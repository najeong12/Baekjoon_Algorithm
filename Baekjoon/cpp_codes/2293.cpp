#include <stdio.h>

int main(){
	int n, k;
	int arr[109], dp[20009];

	scanf("%d %d", &n, &k);
	for(int i=0 ; i<n ; i++)
		scanf("%d", &arr[i]);
	for(int i=0 ; i<=k ; i++)
		dp[i] = 0;
	for(int i=0 ; i<n ; i++){
		if (arr[i]>k) continue;
		dp[arr[i]] += 1;
		for (int j = arr[i]+1 ; j<=k ; j++){
			dp[j] += dp[j-arr[i]];	
		}
	}
	printf("%d\n", dp[k]);
	return (0);
}
		
