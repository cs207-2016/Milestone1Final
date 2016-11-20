import timeseries.TimeSeries as ts
import timeseries.SimilaritySearch as ss


if __name__ == "__main__":
    
    t1 = ss.tsmaker(0.5, 0.1, 0.01)
    t2 = ss.tsmaker(0.5, 0.1, 0.01)
    print(t1.mean(), t1.std(), t2.mean(), t2.std())
    import matplotlib.pyplot as plt
    plt.plot(t1)
    plt.plot(t2)
    plt.show()
    standts1 = ss.stand(t1, t1.mean(), t1.std())
    standts2 = ss.stand(t2, t2.mean(), t2.std())

    idx, mcorr = ss.max_corr_at_phase(standts1, standts2)
    print("IDX, MCORR")
    print(idx, mcorr)
    sumcorr = ss.kernel_corr(standts1, standts2, mult=10)
    print("SUMCORR")
    print(sumcorr)
    t3 = ss.random_ts(2)
    t4 = ss.random_ts(3)
    plt.plot(t3)
    plt.plot(t4)
    plt.show()
    standts3 = ss.stand(t3, t3.mean(), t3.std())
    standts4 = ss.stand(t4, t4.mean(), t4.std())
    idx, mcorr = ss.max_corr_at_phase(standts3, standts4)
    print("IDX, MCORR 2")
    print(idx, mcorr)
    sumcorr = ss.kernel_corr(standts3, standts4, mult=10)
    print("SUMCORR 2")
    print(sumcorr)