import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl

def timeseries_plotting(time, value):

    """
    Plot original time-series.
    Parameter:
      - time: time-series sequence.
      - value: value sequence by time-series.
    """

    plt.figure(figsize=(10,8))
    plt.title("Time-series Plot", fontsize=15)
    plt.plot(time, value, "-", alpha=.6)
    plt.xticks(rotation=45)

def predicted_plotting(train_date, train_value, predicted_date, predicted_value, predicted_conf = [], ground_truth = []):
    
    """
    Plot predicted time-series.
    Parameter:
      - train_date: train time-series date.
      - train_value: train time-series value.
      - predicted_date: test time-series date.
      - predicted_value: test time-series value.
      - predicted_conf = (pred_lower, pred_upper): confidence interval predicted time-series sequence.
      - ground_truth: Ground truth of predicted_value (if exist)
    """
    plt.rc('font', size=12)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(train_date, train_value, color='tab:orange', label='Train')
    ax.plot(predicted_date, predicted_value, color='tab:blue', linestyle = '--', label='Predicted')
    if len(ground_truth) != 0:
      ax.plot(predicted_date, ground_truth, color='tab:green', label='Ground Truth')
    if len(predicted_conf) != 0:
      plt.fill_between(predicted_date, predicted_conf[0], predicted_conf[1], color='blue', alpha=0.1)
    ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
    ax.set_title('Value')
    
    fig.show()
      