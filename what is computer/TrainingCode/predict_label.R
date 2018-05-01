library(nlme)
library(Boruta)
library(randomForest)
model_labels <- list()

ntrees = 501		# Number of trees
ncv = 6		# Number of folds to make cross validation
# and calculated predictions for training data
ntry = 5		# Number of times that cross validation is 
# going to be run.
sets <- c(1)	# set 4 is not included because set 4 does
# not have labels.
#for (SET in sets){
SET=1
  print( paste('SET', SET) )
  model_labels[[SET]] <- list()
  
  training_main <- read.csv(paste('training/training_', SET, '.csv', sep = '')) # It reads main file
  training_w <- read.csv(paste('training/training_', SET, '_w.csv', sep = '')) # It reads file with counts of words
  training_b <- read.csv(paste('training/training_', SET, '_b.csv', sep = '')) # It reads file with counts of bigrams
  training_t <- read.csv(paste('training/training_', SET, '_t.csv', sep = '')) # It reads file with counts of trigrams
  names(training_main)[2:4] <- c('f.x','f2.x','f3.x')
  
  training_label <- read.csv(paste('training/training_', SET, '_label.csv', sep = ''))
  
  label_predictions_training <- data.frame( training_main$Id )
  names( label_predictions_training ) <- c( 'Id' )
  
  label_probabilities_training <- data.frame( training_main$Id )
  names( label_probabilities_training ) <- c( 'Id' )
  
  print('starting')
  
  for (LABEL in 0:17 ){
    print( paste('label', LABEL) )
    
    training_main <- data.frame( cbind( training_label[["Id"]], training_label[[ paste('label_',LABEL, sep ='') ]] ) )
    names(training_main) <- c('Id','LABEL') 
    n_pos <- sum(training_main[['LABEL']]) # Number of essays that contain a certain label.
    if ( n_pos > 3){ # The following is done only if more than 3 essays contain a certain label.
      
      
      training_now <- merge( training_main, training_w, by.x = 'Id', by.y = 'Id')
      training_now <- merge( training_now, training_b, by.x = 'Id', by.y = 'Id')
      training_now <- merge( training_now, training_t, by.x = 'Id', by.y = 'Id')
      row.names(training_now) <- training_now$Id
      
      LoadToEnvironment <- function(RData, env = new.env()){
        load(RData, env)
        return(env) 
      }
      
      word <- LoadToEnvironment('C:/Users/sheoran/Documents/GitHub/Descriptive-Answer-Checking/what is computer/TrainingCode/VariablesSelected/formulas_labels_w.RData' )
      bi <- LoadToEnvironment('C:/Users/sheoran/Documents/GitHub/Descriptive-Answer-Checking/what is computer/TrainingCode/VariablesSelected/formulas_labels_b.RData' )
      tri <- LoadToEnvironment('C:/Users/sheoran/Documents/GitHub/Descriptive-Answer-Checking/what is computer/TrainingCode/VariablesSelected/formulas_labels_t.RData' )
      # The following gets the calculated relevant words, bigrams, and trigrams for each label
      bors1 <- word[["formula_labels"]][[SET]][[LABEL+1]]
      bors1 <- TentativeRoughFix( bors1 )
      form1 <- getConfirmedFormula(bors1)
      bors2 <- bi[["formula_labels"]][[SET]][[LABEL+1]]
      bors2 <- TentativeRoughFix( bors2 )
      form2 <- getConfirmedFormula(bors2)
      bors3 <- tri[["formula_labels"]][[SET]][[LABEL+1]]
      if ( length(which(bors3$finalDecision == 'Confirmed')) > 0){ # This checks if there are important trigrams
        form3 <- getConfirmedFormula(bors3)
        form <- asOneFormula( form1, form3, form2,  omit = 'LABEL')
      }
      
      if ( length(which(bors3$finalDecision == 'Confirmed')) == 0){ # This checks if there are not important trigrams
        form <- asOneFormula( form1, form2,  omit = 'LABEL')
      }
      
      form_s <- all.vars(form)
      form <- as.formula( paste( 'as.factor(LABEL)', '~', paste( form_s, collapse= '+') )  ) # It combines all variables in a formula
      
      mmtry <- 5#max(floor(length(form_s)/3), 1) #Number of variables to try at each split
      
      training_probabilities_list <- list()
      
      for (try in 1:mmtry){ #Loop to run different Cross validations
        
        training_predictions <- data.frame()
        training_probabilities <- data.frame()
        
        n_neg <- nrow(training_main) - n_pos
        
        if ( n_pos <= 30){
          pos_fold <- rep(1:10, times = 2)
          pos_fold <- pos_fold[1:n_pos]
        }
        if ( n_pos > 30){
          pos_fold <- sample(1:ncv, n_pos,replace=TRUE)
        }
        
        neg_fold <- sample(1:ncv, n_neg,replace=TRUE)
        
        ind_pos <- which( training_now[['LABEL']] == 1)
        ind_neg <- which( training_now[['LABEL']] == 0)
        
        tr_pos <- training_now[ind_pos,]
        tr_neg <- training_now[ind_neg,]
        
        
        for (cv in 1:16){ #It runs the cross validation
          
          ind_tr_pos <- which( pos_fold != cv )
          ind_te_pos <- which( pos_fold == cv )
          
          ind_tr_neg <- which( neg_fold != cv )
          ind_te_neg <- which( neg_fold == cv )
          
          traincv_pos <- tr_pos[ind_tr_pos,]
          testcv_pos <- tr_pos[ind_te_pos,]
          traincv_neg <- tr_neg[ind_tr_neg,]
          testcv_neg <- tr_neg[ind_te_neg,]
          
          traincv <- rbind( traincv_pos, traincv_neg)
          testcv <- rbind( testcv_pos, testcv_neg)
          
          #It trains Random Forest for subset of training data
          rf_labels_cv <- randomForest( form, data = traincv, ntree = ntrees, do.trace = 0, importance = TRUE, mtry = mmtry)
          
          #It predicts the probabilities for one fold of training data
          t_prob_cv <- predict( rf_labels_cv, newdata = testcv, type = 'prob')
          t_prob_cv <- as.vector( t_prob_cv[,2] )
          
          # t_pred_cv, and any line making reference to it, is not necessary for final model
          t_pred_cv <- as.numeric( as.vector( predict( rf_labels_cv, newdata= testcv, type = 'response') ) ) 
          
          dafrcv <- data.frame( testcv[['Id']], t_pred_cv )
          training_predictions <- rbind( training_predictions, dafrcv )
          
          dafrcv2 <- data.frame( testcv[['Id']], t_prob_cv )
          training_probabilities <- rbind( training_probabilities, dafrcv2 )
          
        }
        print("random forest 1")
        names(training_predictions) = c( 'Id' , paste( 'PRED_',LABEL, sep ='') )
        names(training_probabilities ) = c( 'Id' , paste( 'PROB_',LABEL, sep ='') )
        training_predictions <- training_predictions[ order( training_predictions$Id ), ]
        training_probabilities <- training_probabilities[ order( training_probabilities$Id ), ]
        row.names(training_predictions) <- training_predictions$Id
        row.names(training_probabilities) <- training_probabilities$Id
        training_probabilities_list[[try]] <- training_probabilities
      }
      
      #It trains Random Forest with complete training data. This Random Forest is used for the test data.
      rf_labels <- randomForest( form, data = training_now, ntree = ntrees, do.trace = 0, importance = FALSE, mtry = mmtry )
      print("Random forest 2")
      #The following lines average the probabilities calculated by each run of the cross validations
      training_probabilities[,2] <- 0.0
      for(try in 1:ntry){
        training_probabilities[,2] <- training_probabilities[,2] +  training_probabilities_list[[try]][,2]
      }
      training_probabilities[,2] <- training_probabilities[,2]/ntry
      
      
      model_labels[[SET]][[LABEL+1]] <- rf_labels #The Random Forest for a label is saved
      
      label_predictions_training <- merge( label_predictions_training, training_predictions, by.x = 'Id', by.y = 'Id')
      label_probabilities_training <- merge( label_probabilities_training, training_probabilities, by.x = 'Id', by.y = 'Id')
      
      
    }
    
  }
  
  # Probabilities and predictions are written in csv files
  write.csv( label_predictions_training, file = paste('training/training_', SET, '_l_pred3.csv', sep = '') )
  write.csv( label_probabilities_training, file = paste('training/training_', SET, '_l_prob3.csv', sep = '') )
  
#}

# The Random Forests, using complete training data, for each label and each set are saved.
save( model_labels, file = '/newTrainedModelFiles/models_labels3.RData' )
