// Автор: М. Нехорошева

#include<iostream>
#include<vector>
#include<cmath>
#include<fstream>
#include<iomanip>
struct Coords
{
	float x = 0;
	float y = 0;
};
float CalculateRadius (Coords a, Coords b)
{
	return sqrt (pow (a.x - b.x, 2) + pow(a.y - b.y, 2));
}
int main()
{
	std::ifstream F ("C:\\Users\\man\\Desktop\\2.txt");
	int iter;
	F >> iter;
	std::vector<Coords> Ships;
	for (int i = 0; i < iter; i++)
	{
		Coords C;
		F >> C.x >> C.y;
		Ships.push_back (C);
	}
	Coords Radar;
	F >> Radar.x >> Radar.y;
	int Radius;
	F >> Radius;
	std::vector<float> Length;
	for (int i = 0; i < iter; i++)
		Length.push_back (CalculateRadius(Ships[i], Radar));
	for (int i = 0; i < Ships.size(); i++)
		if (Length[i] > Radius)
		{
			Length.erase (Length.begin() + i);
			Ships.erase (Ships.begin() + i);
			i--;
		}
	for (int i = 0; i < Ships.size() - 1; i++)
		for (int j = i + 1; j < Ships.size(); j++)
			if (Length[i] > Length[j])
			{
				std::swap (Length[i], Length[j]);
				std::swap (Ships[i], Ships[j]);
			}
	std::cout << std::setprecision(1);
	for (int i =0; i < Ships.size(); i++)
		std::cout << (int)Ships[i].x << "\t" << (int)Ships[i].y << "\n";
	int S = Length[0] * 10;
	std::cout << S / 10 <<"," << S % 10;
					
}





















