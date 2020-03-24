start = proc.time()

source("M4demo.R")

# Choose which time series to forecast
indices = 1:23000 # yearly
#indices = 23001:47000 # quarterly
#indices = 47001:95000 # monthly
#indices = 95001:95359 # weekly
#indices = 95360:99586 # daily
#indices = 99587:100000 # hourly

labels = sapply(indices, function(i) M4[[i]]$st)
labels

forecasts = forecast.M4.demo(labels)
forecasts

print("Writing to dataframe")
for (i in 1:length(indices)) {
	id = names(forecasts)[[i]]
	y_hat = forecasts[[i]]
	if (length(y_hat) < 48) {
		NA_array <- rep(NA, 48 - length(y_hat))
		y_hat <- c(y_hat, NA_array)
	}
	print(y_hat)
	if (i == 1) {
		df <- data.frame(y_hat)
	} else {
		df <- cbind(df, y_hat)
	}
	names(df)[i] = id
}

df = t(df)

# Saving the forecast in the root directory of the docker container
setwd("..")
write.csv(df, "y_hat.csv")
read.csv("y_hat.csv")

end = proc.time()
total_time = end - start
print("Total time for run:")
print(total_time)
