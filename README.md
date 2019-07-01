# Privacy-aware-learning

## Quick Reference
### Some functions used and what the parameters mean:

- genData(mu, sigma, n, d) -> returns X(nxd) and y(nx1)
      mu - mean of synthetic data
      sigma - Std Dev. of synthetic data
      n - entries
      d - features
      
- l1norm_X_and_y_preserve_linearity(X, y, val) -> Returns normalised X and y 
      X gets l1 normalised, y gets normalised based on value of val.
      X and y -> data to be l1 normalised
      val = 1 => y gets l1 normalised else y gets max.normalised
      
- priv_plotter(X, y, n, d, k, epsilon, jump, rep, apply_u, apply_v) -> return ans
      X and y -> dataset(generated)
      n -> entries
      d -> features
      k -> k-fold value
      epsilon -> privacy budget
      jump -> Tells how many points are to be obtained to plot the graph(10,20 etc)
      rep -> No of times the noises have to calucated to obtain multiple errors and average them. Reduces peakiness of perturbed                                                                                                     
             input data a bit. Optimium value 10-20. Can go upto 50 for smaller dataasets as time won't be an issue.
      apply_u -> Set as 1 to apply noise to xTx
      apply_v -> Set as 1 to apply noise to xTy
      Returns:
      ans[0] -> Trainset size for x-axis to plot
      ans[1] -> RMSE for a given privacy budget
      ans[2] -> priv.RMSE Standard deviation(SD of ans[1]. Can be use to plot yerr in errorbar)
      ans[3] -> Non private RMSE
      ans[4] -> Non priv.RMSE Standard deviation(SD of ans[3]. Can be use to plot yerr in errorbar)
      ans[5] -> Private Spearman's Rank Correlation Coefficient
      ans[6] -> Non Private Spearman's Rank Correlation Coefficient
      
     
             

