#include "Projekt_FS.h"
 
int ilosc_poludnikow;
int ilosc_rownoleznikow;
double promien_ziemi;
double pi;
double szerokosc_kontowa_biegunow_przez_2;
double stala_sloneczna;
double stala_Stefana_Boltzmana;
double wspulczynnik_reemisji;//globalne ocieplenie
double wsp_dyf;
int fun_slonce;
int fun_emisja;
int fun_wymiana_ciepla;
double albedo_parametr_lad;
double albedo_parametr_morze;
int albedo_rodzaj;
int ilosc_wywolan;
double cieplo_wlasciwe_lad;
double cieplo_wlasciwe_morze;
int czyt_mape_swiata;
int aargc;
char ** aargv;

int main (int argc,char ** argv)
{

aargc=argc;
aargv=argv;

ilosc_poludnikow=100;
ilosc_rownoleznikow=100;
promien_ziemi=6300;
pi=3.1415;
szerokosc_kontowa_biegunow_przez_2=0.1;
stala_sloneczna=1300;
stala_Stefana_Boltzmana=5.67*pow(10,-8);
wspulczynnik_reemisji=0.8;
wsp_dyf=0.5;
fun_slonce=1;
fun_emisja=1;
fun_wymiana_ciepla=0;
albedo_parametr_lad=0.2;
albedo_parametr_morze=0.5;
albedo_rodzaj=1;
ilosc_wywolan=1000;
cieplo_wlasciwe_lad=100000;
cieplo_wlasciwe_morze=300000;
czyt_mape_swiata=0;

if(argc>1)ilosc_poludnikow=atof(argv[1]);
if(argc>2)ilosc_rownoleznikow=atof(argv[2]);
if(argc>3)stala_sloneczna=atof(argv[3]);
if(argc>4)wspulczynnik_reemisji=atof(argv[4]);
if(argc>5)wsp_dyf=atof(argv[5]);
if(argc>6)fun_slonce=atof(argv[6]);
if(argc>7)fun_emisja=atof(argv[7]);
if(argc>8)fun_wymiana_ciepla=atof(argv[8]);
if(argc>9)albedo_parametr_lad=atof(argv[9]);
if(argc>10)albedo_parametr_morze=atof(argv[10]);
if(argc>11)albedo_rodzaj=atof(argv[11]);
if(argc>12)ilosc_wywolan=atof(argv[12]);
if(argc>13)cieplo_wlasciwe_lad=atof(argv[13]);
if(argc>14)cieplo_wlasciwe_morze=atof(argv[14]);
if(argc>15)czyt_mape_swiata=atof(argv[15]);

	const string nazwa_pliku="plik_zapisu.txt";
	Pole b_polnocny(0,0,0.31,cieplo_wlasciwe_lad,0.5,300,0),b_poludniowy(0,0,0.31,cieplo_wlasciwe_lad,0.5,300,0);
	b_polnocny.ref_pole_powiezchni()=pi*pow(promien_ziemi*sin(szerokosc_kontowa_biegunow_przez_2),2);
	b_poludniowy.ref_pole_powiezchni()=pi*pow(promien_ziemi*sin(szerokosc_kontowa_biegunow_przez_2),2);
	Tablica_Pol tab;
	if(czyt_mape_swiata)czytaj_mape_swiata("swiat.txt",tab);
	//exit(0);


	
	Czas czas;
	for(int j=0;j<100;++j)
	{
		akcja_w_min(tab,b_polnocny,b_poludniowy,czas,1);
	}
	for(int j=0;j<ilosc_wywolan;++j)
	{
		akcja_w_godz(tab,b_polnocny,b_poludniowy,czas,1);
	}
	cout<<czas.rok_dzien_godzina_minuta()<<endl;
	cout<< "srednia temperatura:  "<<"<avr_temp>" <<tab.srednia_temperatura()<<"</avr_temp>" << endl;
	/*for(int i=0;i<ilosc_rownoleznikow;++i)
	{
		for(int j=0;j<ilosc_poludnikow;j+=20)
		{//	int j=0;
			cout<<tab.tab_pol_row[j][i].temperatura()<<"  ";
		}	
		cout<<endl;
		
	}*/
	/*for(int i=0;i<ilosc_rownoleznikow;++i)
	{
		for(int j=0;j<ilosc_poludnikow;++j)
		{
			cout<<tab.tab_pol_row[j][i].poludnik()<<","<<tab.tab_pol_row[j][i].rownoleznik()<<" ";
		}	
		cout<<endl;
		
	}*/
	
	//znacznik
	
	//tab.tab_pol_row[50][12].ref_energia_wew()=0;
	

	//zapisz(nazwa_pliku,tab,b_polnocny,b_poludniowy);
//cout <<"wywolanie zapisuj_temperature_srednio_i_arg_wywolania\n";
	zapisuj_temperature_srednio_i_arg_wywolania("plik_do_wykresow.txt",tab);
	rysuj_ziemie_jako_jajko("temperatura_0.txt",tab)	;
}
