#pragma once

/*本番環境*/
//#define NSTEPS 1500000000
/*ローカルサーバ*/
#define NSTEPS 200000
#define NDEVIDE 100000
#define NWRITE (NSTEPS/NDEVIDE)
/*配列の合計*/
template <class T> T array_sum(T array[]){
	T sum=0;
	for(int i=0;i<NUM;i++){
		sum+=array[i];
	}
	return sum;
}
/*関数プロトタイプ宣言*/
void boundary(int NP, double RX[], double LX) ;

void elastic(int NP, double RY[], double VY[], double LY);

void gmap_create(int NP, double RX[], double RY[], double L_GX, double L_GY, int N_GX, int N_GY, int NEIGHBOR_ROW[], int NEIGHBOR_COL[], int NEITGHBOR_LEN, int PAIRLIST[][10], double LX, int **G_MAP);

void force(int NP, double RX[], double RY[], double AX[], double AY[], double LX, double LY, int PAIRLIST[][10], double RC2, double* POT, double* POT_IJ, double* MINI);

void heatwall(double H,int NP,double RY[],double RY_B[],double VY[],double *Q_IN,double *Q_OUT ,double PPY,double PPV,double TEMP_L,double TEMP_H,double *FPP,double LY,double *h_ss,double *d_w);

void piston_move_u(int NP,double RY[],double RY_B[],double VY[],double VY_B[],double AY[],double H,double H_REV,double *Q_IN,double *Q_OUT,double Q_IN_SUM,double Q_OUT_SUM,double DPY,double DPY_B,double *DPV,int *HIT_PISTON,int *THROUGH_PISTON,double *FDP,double TEMP_L,double TEMP_H,double *H1_D,double Momentum_u[2],double Kin_u[2],int *k,int *j,double MDP,double *delta_mom,double *delta_kin,double PROBABIRITY);

void piston_move_d(int NP,double RY[],double RY_B[],double VY[],double VY_B[],double AY[],double H,double H_REV,double *Q_IN,double *Q_OUT,double Q_IN_SUM,double Q_OUT_SUM,double DPY,double DPY_B,double *DPV,int *HIT_PISTON,int *THROUGH_PISTON,double *FDP,double TEMP_L,double TEMP_H,double *H1_D,double Momentum_d[2],double Kin_d[2],int *kk,int *jj,double MDP,double *delta_mom,double *delta_kin,double PROBABIRITY);

void velocity(int NP,double RY[],double VX[],double VY[],double DPY,double *TEMP_D,double *TEMP_U,int *ND,int*NU ,int N_U_list[],double *TEMP);

void partition(double RY[],double VX[] , double VY[] ,double PPY,double TEMP_PART_LIST[NWRITE][PARTNUM],double PRESS_PART_LIST[NWRITE][PARTNUM],int T_WRITE);