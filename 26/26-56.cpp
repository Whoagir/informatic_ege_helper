// �����: �. ����������

#include<bits/stdc++.h>
using namespace std;
int main()
{
	fstream fin("26-56.txt");
	int V,//����� ������� �����
	K,    //���������� ������
	N;    //���������� ������
	//������ ������
	fin>>V>>K>>N;
	int data[N];
	for (int i=0;i<N;i++)
		fin>>data[i];
	sort(data,data+N, greater<int>());
	//reverse(data,data+N);//��������� �� ��������
	
	//�������� ���������
	int free_space[K];//������� ����� �������� � ������ �����
	for(int i=0;i<K;i++)
	{
		free_space[i]=V;
	}
	int file_count=0,//������� ������ �������� � �������
	memory_count=0;//������� �������� �������� � �������
	int disk_index=0;//������ ���� �����, ������� ���������������
	
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
