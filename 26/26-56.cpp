// Автор: М. Нехорошева

#include<bits/stdc++.h>
using namespace std;
int main()
{
	fstream fin("26-56.txt");
	int V,//Объём каждого диска
	K,    //Количество дисков
	N;    //Количество файлов
	//Вводим данные
	fin>>V>>K>>N;
	int data[N];
	for (int i=0;i<N;i++)
		fin>>data[i];
	sort(data,data+N, greater<int>());
	//reverse(data,data+N);//Сортирует по убыванию
	
	//Проводим симуляцию
	int free_space[K];//Сколько места осталось в каждом диске
	for(int i=0;i<K;i++)
	{
		free_space[i]=V;
	}
	int file_count=0,//Сколько файлов осталось в локалке
	memory_count=0;//Сколько мегабайт осталось в локалке
	int disk_index=0;//Индекс того диска, который рассматривается
	
	for(int i=0;i<N;i++)
	{
		if(free_space[disk_index]>=data[i])
		{
			free_space[disk_index]-=data[i];
			disk_index+=1;
			if(disk_index==K)disk_index=0;
		}
		else
		{
			int j=0;
			for(;j<K;j++)
			{
				disk_index++;
				if(disk_index==K)disk_index=0;
				if(free_space[disk_index]>=data[i])
				{
					free_space[disk_index]-=data[i];
					break;
				}
			}
			if(j==K)
			{
				file_count+=1;
				memory_count+=data[i];
			}
		}
	}
	cout<<file_count<<" "<<memory_count<<endl;
}
