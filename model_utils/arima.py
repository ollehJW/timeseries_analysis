import pmdarima as pm
from pmdarima.arima import ndiffs
import matplotlib.pyplot as plt
import numpy as np 

class ARIMA_Model(object):

    """
    Build Auto Arima model. 
    Parameter:
      - time: time-series sequence.
      - diff: 차분. (Default: 1)
      - seasonal: 계절성 요인 고려 여부. (Default: False)
      - m: 계절성 주기. (Default: 1)
      - n_periods: 예측하고자 하는 시계열 수.
    """

    def __init__(self, time):
        self.time = time
    
    def estimate_diff(self):
        kpss_diffs = ndiffs(self.time, alpha=0.05, test='kpss', max_d=6)
        adf_diffs = ndiffs(self.time, alpha=0.05, test='adf', max_d=6)
        n_diffs = max(adf_diffs, kpss_diffs)
        print("적절 차분: {}".format(n_diffs))
        return n_diffs
    
    def build_model(self, diff = 1, seasonal = False, m = 1):
        self.model = pm.auto_arima(y = self.time, d = diff, start_p = 0,
                        max_p = 5, start_q = 0, max_q = 5,
                        m = m, seasonal = seasonal,
                        stepwise = True, trace=True)
        self.model.fit(self.time)

    def summary(self):
        print(self.model.summary())

    def plot_diagnostics(self):
        self.model.plot_diagnostics(figsize=(16, 8))
        plt.show()
    
    def forecast_one_step(self):
        fc, conf_int = self.model.predict(n_periods=1 # 한 스텝씩!
            , return_conf_int=True)              # 신뢰구간 출력
        return (
            fc.tolist()[0],
            np.asarray(conf_int).tolist()[0]
        )

    def predict(self, n_periods, time_test = []):
        pred = []
        pred_upper = []
        pred_lower = []

        for iter in range(n_periods):
            fc, conf = self.forecast_one_step()
            pred.append(fc)
            pred_upper.append(conf[1])
            pred_lower.append(conf[0])

            ## 모형 업데이트 !!
            if len(time_test) > 0:
                self.model.update(time_test[iter])
            else:
                self.model.update(fc)

        return (pred, pred_upper, pred_lower)
