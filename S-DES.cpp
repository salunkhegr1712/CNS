#include<iostream>
#include <bits/stdc++.h>
using namespace std;


void permutation1(int key[]){

   int permutation_10[10] = {3,5,2,7,4,10,1,9,8,6};
   int temp[10] = {0};
   
   for(int  i = 0 ; i < 10 ; i++){
        temp[i] = key[i];
   }
   
   for(int i = 0 ; i < 10 ; i++){
       key[i] = temp[permutation_10[i]-1];
   }
}


void permutation2(int key[]){
    
    int permutation_8[8] = {6,3,7,4,8,5,10,9};
    int temp[10] = {0};
    
    for(int i = 0 ; i< 10 ; i++){
        temp[i] = key[i];
    }
    
    for(int i= 0 ; i< 8 ; i++){
       key[i] = temp[permutation_8[i] -1];
    }
}

//function to perform left shift according to round number
void lshift(int lhalf[], int rhalf[], int shift){
    
    int temp_l = lhalf[0];
    int temp_r = rhalf[0];
    
    for(int i = 0 ; i < 4 ; i++){
        lhalf[i] = lhalf[i+1];
        rhalf[i] = rhalf[i+1];
    }
    
    lhalf[4] = temp_l;
    rhalf[4] = temp_r;
    
    if(shift == 2){
       lshift(lhalf,rhalf,1);
    }
}

//function to perform key generation
int* key_generation(int key[], int round){
  
  int lhalf[5], rhalf[5];
  static int key1[10], key2[8];
  
  //perform p10 permutation on key
  permutation1(key);
  
  for(int i = 0 ; i< 10 ; i++){
     if(i < 5){
        lhalf[i] = key[i];
     }
     else{
        rhalf[i-5] = key[i];
     }
  }
  
  //left shift both half by one
  lshift(lhalf,rhalf,1);
  
  //combine both half to form key
  for(int i=0;i<5;i++)	
	{
		key1[i]=lhalf[i];
		key1[i+5]=rhalf[i];
	}
		
  if(round==1)
	{
		permutation2(key1);
		return key1;
	}
  else{
         //left shift by one place again 
         lshift(lhalf,rhalf,2);
         //combine both half
         for(int i=0;i<5;i++)	
	{
		key2[i]=lhalf[i];
		key2[i+5]=rhalf[i];
	}
	permutation2(key2);
	return key2;
  } 
}


//Encryption process

//function to perform initial permutation
void initial_permutation(int plainText[]){
     int temp[8];
     int out[8] = {2,6,3,1,4,8,5,7};
     
     for(int i = 0 ; i < 8 ; i++){
       temp[i] = plainText[i];
     } 
     cout<<"\n";
     cout<<"\nInitial Permutation : "<<endl;
     for(int i = 0 ; i< 8 ; i++){
       plainText[i]=temp[out[i]-1];
       cout<<plainText[i]<<"\t";
       }
       
}

//function to perform inverse initial permutation
void inversefirstpermutation(int plainText[]){
     int temp[8];
     int out[8] = {2,6,3,1,4,8,5,7};
     
     for(int i = 0 ; i < 8 ; i++){
       temp[i] = plainText[i];
     } 
     
     for(int i = 0 ; i< 8 ; i++){
       plainText[out[i]-1]=temp[i];
       cout<<plainText[i]<<"\t";
       }
}

//function to perform expansion permutation on right half of key.Here 4 bits converted to 8 bits
int* expandedPermutation(int rhalf[])
{
	int out[8]={4,1,2,3,2,3,4,1};
	int temp[4];
	static int exRight[8];

	for(int i=0;i<4;i++)	
		temp[i]=rhalf[i];

	for(int i=0;i<8;i++)
	{
		exRight[i]=temp[out[i]-1];
		cout<<exRight[i]<<"\t";
	}
	return exRight;
}

//Substitution box S0
int get_S0(int row,int column)
{
	int s0[4][4]={ {01,00,11,10},
			{11,10,01,00},
			{00,10,01,11},
			{11,01,11,10}};
	return s0[row][column];
}

//Substitution box S1
int get_S1(int row,int column)
{
	int s1[4][4]={ {00,01,10,11},
			{10,00,01,11},
			{11,00,01,00},
			{10,01,00,11}};
	return s1[row][column];
}

//function to perform p4 permutation	
void p4_permutation(int s0s1[])
{
	int out[4]={2,4,3,1};
	int temp[4];

	for(int i=0;i<4;i++)		//backup array
		temp[i]=s0s1[i];

	for(int i=0;i<4;i++)
	{
		s0s1[i]=temp[out[i]-1];
	}

}

static int r1key[8],r2key[8];

//function to perform different round while encryption and decryption
int* round(int plaintext[], int key[], int round_number, int flag){
     
     int left[4],right[4],*exRight,s0[4],s1[4],temp_key[10];
     
       cout<<"\n\nText to be decodingd:\n";
	for(int i=0;i<8;i++)
	{
		cout<<plaintext[i];
	}
     
     cout<<"\nROUND-"<<round_number;
     cout<<"\n";
     cout<<"\nKey-"<<endl;
     for(int i=0;i<10;i++)
	{	
		cout<<key[i]<<"\t";
		temp_key[i]=key[i]; //backup of key		
	}
	
	if(round_number==1){
	
	//step 1: initial permutation of plain text
	initial_permutation(plaintext);
	}
	
	cout<<"\n\nleft half:\n";
	//divide into two halves
	for(int i=0;i<4;i++)
	{
		left[i]=plaintext[i];
		right[i]=plaintext[i+4];
		//cout<<left[i];
	}
	
	exRight= expandedPermutation(right);
	cout<<"\n\nexRight:\n";
	for(int i=0;i<8;i++)
		cout<<exRight[i];	

	
       static int* key1;
       //flag=0 is for encoding
	if(flag==0)		
	{	key1=key_generation(key,round_number);
		if(round_number==1)
		{
			for(int i=0;i<8;i++)
				r1key[i]=key1[i]; //backup key
		}
		else
		{
			for(int i=0;i<8;i++)
				r2key[i]=key1[i];	
		}
		cout<<"\n\nencoding Key of Round "<<round_number<<endl;
		for(int i=0;i<8;i++)
		{	
			cout<<key1[i];
		}
	}
	//else flag=1 ie. for decoding
	else			
	{
		cout<<"\n\n\nInside decoding : ";
		//for decoding we use the keys in reverse order
		//if round1 use key2
		if(round_number==1)
		{
			cout<<"\nInside round1: ";
			for(int i=0;i<8;i++)
			{
				key1[i]=r2key[i];
				//cout<<r2key[i];
			}
		}
		//if round2 use key1
		else				
		{
			cout<<"\nInside round2";
			for(int i=0;i<8;i++)
			{
				//cout<<r1key[i];
				key1[i]=r1key[i];
			}
		}	
		
		cout<<"\n\ndecoding Key of Round "<<round_number<<endl;
		for(int i=0;i<8;i++)
		{	
			cout<<key1[i];
		}
	}
       
       cout<<"\n\nExpanded right\n";
	for(int i=0;i<8;i++)
	{
		cout<<exRight[i]<<"\t";
	}
	cout<<"\n\n";
	//perform XOR between key and expanded right part of key
	for(int i=0;i<8;i++)
	{
		exRight[i]=exRight[i] ^  key1[i];
		if(i<4)
			s0[i]=exRight[i];
		else
			s1[i-4]=exRight[i];
	}
	
	int row=s0[3]+(s0[0]*2);			//step 4
	int column=s0[2]+(s0[1]*2);
	static int s0s1[4];
	int ss0=get_S0(row,column);
	//cout<<"\nRow: "<<row<<"Column: "<<column;
	row=s1[3]+(s1[0]*2);
	column=s1[2]+(s1[1]*2);
	//cout<<"\nRow: "<<row<<"Column: "<<column;
	int ss1=get_S1(row,column);

	s0s1[1]=ss0%10;
	s0s1[0]=ss0/10;
	s0s1[3]=ss1%10;
	s0s1[2]=ss1/10;

	cout<<"\n\nBefore P4:\n";
	for(int i=0;i<4;i++)
		cout<<s0s1[i];
	p4_permutation(s0s1);
	
	static int new_plainText[8];
	//s0s1 EXOR lhalf from step 1
	for(int i=0;i<4;i++)
	{
		s0s1[i]=s0s1[i] ^ left[i];
		//swap the s0s1 and right half from step 1 to generate plain text for next round
		//if round is not 2nd one and it's not for decoding
		if(round_number!=2)		
		{
			new_plainText[i]=right[i];
			new_plainText[i+4]=s0s1[i];
		}
		//else don't swap
		else							
		{
			new_plainText[i+4]=right[i];
			new_plainText[i]=s0s1[i];	
		}
	}

	cout<<"\n\ns0s1:\n";
	for(int i=0;i<4;i++)
		cout<<s0s1[i];
	
	cout<<"\n\nRound "<<round_number<<" Output:\n";
	if(round_number == 1){
	  for(int i=0;i<8;i++)
		 cout<<new_plainText[i]<<"\t";
	  cout<<endl;
	}

	if(round_number==1)
	{
		cout<<"\n\ngoing for next round\n";
		//if encoding
		if(flag==0)		
			round(new_plainText,temp_key,2,0);
	        //else decoding		
		else			
			round(new_plainText,temp_key,2,1);
	}
	//else
	
		//return new_plainText;
		
        return new_plainText;
	
}


//function to perform encrryption
int* encoding(int pt[],int* round_text,int key[])
{
	round_text=round(pt,key,1,0);
	inversefirstpermutation(round_text);

	cout<<"\n\n-------------FINAL CIPHER TEXT-------------\n";
	for(int i=0;i<8;i++)
		cout<<round_text[i];

	return round_text;
}

//function to perofrm deryption
void decoding(int pt[], int* cipher_text,int key[])
{
	int *new_ct=round(cipher_text,key,1,1);		//flag=1 for decoding
	inversefirstpermutation(new_ct);

	cout<<"\n\n-------------decodingD TEXT-------------\n";
	for(int i=0;i<8;i++)
		cout<<new_ct[i];
        cout<<"\n";
}

int main()
{
	int *round_text, *cipher_text, ptext[8],key[10];
	cout<<"\nEnter the plain text (8-bits) :";
	for(int i=0;i<8;i++)
		cin>>ptext[i];
	cout<<"\nEnter the key (10-bits) :";
	for(int i=0;i<10;i++)
		cin>>key[i];
	
	time_t start1, end1,start2,end2;
	time(&start1);
	cout<<"\n-------------ENCRYPTION-------------\n";
	cipher_text=encoding(ptext,round_text,key);		//Encryption
	time(&end1);
	time(&start2);
	cout<<"\n\n\n-------------DECRYPTION-------------\n";
	decoding(ptext,cipher_text,key);
	time(&end2);					//Decryption
	double t_t = double(end1 - start1);
	cout << "\nTime taken for Encryption is : "<< t_t << setprecision(4);
	cout << " sec " << endl;
	double t_t1 = double(end2 - start2);
	cout << "\nTime taken for Decryption is : "<< t_t1 << setprecision(4);
	cout << " sec " << endl;
	return 0;
}
