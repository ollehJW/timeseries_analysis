# %%
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# %%

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

# %%
def predicted_plotting(train, predicted, predicted_conf, test = []):
    
    """
    Plot predicted time-series.
    Parameter:
      - train: train time-series sequence.
      - predicted: predicted time-series sequence.
      - predicted_conf = (pred_lower, pred_upper): confidence interval predicted time-series sequence.
      - test: test time-series sequence. (if exist)
    """

    fig = go.Figure([
    # 훈련 데이터-------------------------------------------------------
    go.Scatter(x = train['Date'], y = train['Value'], name = "Train", mode = 'lines'
              ,line=dict(color = 'royalblue'))
    # 테스트 데이터------------------------------------------------------
    , go.Scatter(x = test['Date'], y = test['Value'], name = "Test", mode = 'lines'
                ,line = dict(color = 'rgba(0,0,30,0.5)'))
    # 예측값-----------------------------------------------------------
    , go.Scatter(x = predicted['Date'], y = predicted['Value'], name = "Prediction", mode = 'lines'
                     ,line = dict(color = 'red', dash = 'dot', width=3))
    
    # 신뢰 구간---------------------------------------------------------
    , go.Scatter(x = test['Date'].tolist() +test['Date'][::-1].tolist() 
                ,y = predicted_conf[1] + predicted_conf[0][::-1] ## 상위 신뢰 구간 -> 하위 신뢰 구간 역순으로
                ,fill='toself'
                ,fillcolor='rgba(0,0,30,0.1)'
                ,line=dict(color='rgba(0,0,0,0)')
                ,hoverinfo="skip"
                ,showlegend=False)
                ])
    
    fig.update_layout(height=400, width=1000, title_text="ARIMA Prediction")
    fig.show()
      