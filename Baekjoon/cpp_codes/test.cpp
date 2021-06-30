#include <iostream>
#include <vector>

int wid, hei;
long long result;
std::vector<std::vector<int> > paper;

using namespace std;

void output()
{
	std::cout << result;
}

void solution()
{
	int und, fnb, lnr;

	und = fnb = lnr = 0;

	// up & down
	und = wid * hei * 2;

	// fnb & back
	for(int i = 1 ; i <= wid ; ++i)
		for(int j = 1 ; j <= hei + 1 ; ++j){
            // cout << "i j" << i << j << endl;
			fnb += std::abs(paper[j][i] - paper[j - 1][i]);
            // cout << std::abs(paper[j][i] - paper[j - 1][i]) << endl;
        }
        // std::cout << "fnb" << fnb << endl;

	//left & right
	for(int i = 1 ; i <= hei ; ++i)
		for(int j = 1 ; j <= wid + 1 ; ++j){
            // cout << "i j" << i << j << endl;
			lnr += std::abs(paper[i][j] - paper[i][j - 1]);
            // cout << std::abs(paper[i][j] - paper[i][j - 1]) << endl;
        }
        // std::cout << "lnr" << lnr << endl;
	result = und + fnb + lnr;
	// std::cout << "all : " << und + fnb + lnr << std::endl;
    
}

void input()
{
	std::cin >> wid >> hei;
	paper.resize(hei + 2, std::vector<int>(wid + 2, 0));
	for(int i = 1 ; i <= hei ; ++i)
		for(int j = 1 ; j <= wid ; ++j)
			std::cin >> paper[i][j];
}

void preset()
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(0);
	std::cout.tie(0);
}

int main()
{
	preset();
	input();
	solution();
	output();
}