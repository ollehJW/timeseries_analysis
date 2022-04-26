# %%
from preprocess_utils.data_utils import load_data, datetime_convert, data_split
from preprocess_utils.normalization import Normalize
from visualize_utils.visualize import timeseries_plotting, predicted_plotting
from model_utils.arima import ARIMA_Model
import pandas as pd
# %%
filename = "/home/jongwook95.lee/study/timeseries_analysis/data/example.csv"
data = load_data(filename, encoding = 'euc-kr')
data.head()
# %%
data = datetime_convert(data, '일자', format = "%Y/%m/%d")
data = data.sort_values(by = '일자').reset_index(drop = True)
# %%
timeseries_plotting(data['일자'], data['종가'])

# %%
(train, test) = data_split(data, '일자', by = 'time', time_sep = '2020-01-01')
train.head()

# %%
arima_model = ARIMA_Model(train['종가'])
arima_model.estimate_diff()
arima_model.build_model(diff = 1, seasonal = False)
# %%
arima_model.summary()
# %%
arima_model.plot_diagnostics()
# %%
(pred, pred_upper, pred_lower) = arima_model.predict(len(test['일자']), time_test = test['종가'])
# %%
true_train = pd.DataFrame({'Date': train['일자'], 'Value': train['종가']})
true_test = pd.DataFrame({'Date': test['일자'], 'Value': test['종가']})
pred_test = pd.DataFrame({'Date': test['일자'], 'Value': pred})

# %%
predicted_plotting(true_train, pred_test, [pred_lower, pred_upper], true_test)
# %%
