start = proc.time()

print("Loading libraries")

library(M4metalearning)
library(M4comp2018)

print("Assigning training set")
indices <- 1:100000

# Collect the indices of the unwanted time series in unvalid_indices
unvalid_indices = vector()
unvalid_ts = c("Y12146", "Y21168", "Y22801", "Q5619", "M16993", "D2085")
for (i in indices) {
    id = M4[[i]]$st
    if (id %in% unvalid_ts) {
        unvalid_indices = c(unvalid_indices, i)
    }
}

# Delete the unvalid_indices from the indices
for (i in length(indices):1) {
    index = indices[i]
    if (index %in% unvalid_indices) {
        indices = indices[-i]
    }
}

M4_train <- M4[indices]
for (i in 1:length(indices)) {
    print(M4_train[[i]]$st)
}

print("Removing test values from training set")
M4_train <- temp_holdout(M4_train)

print("Calculating forecast for training set using nine different forecasting methods")
M4_train <- calc_forecasts(M4_train, forec_methods(), n.cores=8)

print("Calculating errors")
M4_train <- calc_errors(M4_train)

print("Calculating features")
M4_train <- THA_features(M4_train, n.cores=8)

print("create_feat_classif_problem")
train_data <- create_feat_classif_problem(M4_train)

print("Train a meta-model given the errors and features of the nine different forecasts")
meta_model <- train_selection_ensemble(train_data$data, train_data$errors)

print("Calculating forecast for test set using nine different forecasting methods")
M4_test <- M4[indices]
M4_test <- calc_forecasts(M4_test, forec_methods(), n.cores=8)
M4_test <- THA_features(M4_test, n.cores=1)
test_data <- create_feat_classif_problem(M4_test)

print("Using meta-model to combine the nine different forecasts for the test set to one final forecast")
preds <- predict_selection_ensemble(meta_model, test_data$data)
M4_test <- ensemble_forecast(preds, M4_test)

print("Writing to dataframe")
for (i in 1:length(indices)) {
        id <- c(M4_test[[i]]$st)
        y_hat <- M4_test[[i]]$y_hat
        if (length(y_hat) < 48) {
                NA_array <- rep(NA, 48 - length(y_hat))
                y_hat <- c(y_hat, NA_array)
        }
        if (i == 1) {
                df <- data.frame(y_hat)
        } else {
                df <- cbind(df, y_hat)
        }
        names(df)[i] = id
}

df = t(df)
write.csv(df, "y_hat.csv")

end = proc.time()
total_time = end - start
print("Total time for run:")
print(total_time)
