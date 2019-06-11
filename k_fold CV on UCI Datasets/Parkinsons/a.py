plotnum = 1
    for i in range(len(entries)):
        for j in range(len(features)):
            
            feature = features[j]
            d = feature
            entry = entries[i]
            elems = (d*(d+1))/2
            jump = math.floor(entry / 10)
            
            X,y = totalX[0:entry, 0:feature], totaly[0:entry]
        
            # X = normalize(X, norm='l1')
            # y = y/sum(abs(y))
        
            X = normalize(X, norm='l2')
            RMS = (sum(y**2))**0.5
            y = y/RMS
        
            X_with_bias = np.append(arr=np.ones((X.shape[0],1)) , values=X , axis=1)
            xT = X_with_bias.transpose()
            xTx = np.dot(xT, X_with_bias)
            xTy = np.dot(xT, y)           
            
            ans = k_fold_plot_RMSE_vs_training_set_size_params(X, y, k, feature, jump, entry)
            
            plt.subplot(8,2,plotnum)
#             plt.errorbar(ans[0], ans[1], yerr=ans[2], color=colors[4], ecolor=colors[4], capsize=3, label='NP')
            plt.scatter(ans[0], ans[1], color=colors[4], s=10)
            
            
            for l in range(len(epsilon)):
#                 plt.subplot(8,2,plotnum)
#                 plt.errorbar(ans[0], ans[1], yerr=ans[2], color=colors[4], ecolor=colors[4], capsize=3, label='NP')
                plt.scatter(ans[0], ans[1], color=colors[4], s=10)
#                 b1 = 1/(epsilon[l]*elems)
#                 b2 = 1/(epsilon[l]*d)
            
#                 u = np.random.laplace(loc=0.0, scale=b1, size=(d+1)*(d+1)).reshape(d+1, d+1)
#                 v = np.random.laplace(loc=0.0, scale=b2, size=d+1)
            
#                 sTs = xTx + u
#                 sTt = xTy + v
            
#                 sTspinv = np.linalg.pinv(sTs)
#                 wi = np.dot(sTspinv, sTt)
            
#                 xTxpinv = np.linalg.pinv(xTx)
#                 w = np.dot(xTxpinv, xTy)

#                 T = np.dot(X_with_bias, wi)
                
#                 ans = k_fold_plot_RMSE_vs_training_set_size_params(X, T, k, feature, jump, entry)
                
#                 plt.errorbar(ans[0], ans[1], yerr=ans[2], color=colors[l], ecolor=colors[l], capsize=3, label=epsilon[l])
#                 plt.scatter(ans[0], ans[1], color=colors[l], s=10)
            
            plt.xlabel("Training set size")
            plt.ylabel("RMSE")
            plt.tight_layout()
            plt.show()
            plotnum = plotnum+1