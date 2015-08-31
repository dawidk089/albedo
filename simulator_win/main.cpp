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
bool fun_czytaj;
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
wspulczynnik_reemisji=0.52;
wsp_dyf=300;
fun_slonce=1;
fun_emisja=1;
fun_wymiana_ciepla=1;
albedo_parametr_lad=0.34;
albedo_parametr_morze=0.27;
albedo_rodzaj=0;
ilosc_wywolan=200;
cieplo_wlasciwe_lad=100000;
cieplo_wlasciwe_morze=300000;
czyt_mape_swiata=1;
fun_czytaj=0;

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
if(argc>16)fun_czytaj=atof(argv[16]);

	const string nazwa_pliku="PLIKI_TXT\\plik_zapisu.txt";
	Pole b_polnocny(0,0,0.31,cieplo_wlasciwe_lad,0.5,300,0),b_poludniowy(0,0,0.31,cieplo_wlasciwe_lad,0.5,300,0);
	b_polnocny.ref_pole_powiezchni()=pi*pow(promien_ziemi*sin(szerokosc_kontowa_biegunow_przez_2),2);
	b_poludniowy.ref_pole_powiezchni()=pi*pow(promien_ziemi*sin(szerokosc_kontowa_biegunow_przez_2),2);
	Tablica_Pol tab;
	Czas czas;


	if(czyt_mape_swiata)
		czytaj_mape_swiata("PLIKI_TXT\\swiat.txt",tab);


	//BARDZO WA¯NA FUNKCJA - DECYDYJE CZY ZCZYTUJE STAN POCZADKOWY Z JAKIEGOŒ PLIKU CZY ZACZYNA OD ZERA
	if(fun_czytaj)
		czytaj(nazwa_pliku,tab,b_polnocny,b_poludniowy,czas);
	else
	for(int j=0;j<60;++j)
	{
		akcja_w_min(tab,b_polnocny,b_poludniowy,czas,1);
	}
	


	int zapis_co_n=1;
	wspulczynnik_reemisji=0;
	for(int i=0;i<19;++i)
	{
	wspulczynnik_reemisji+=0.05;
	czytaj(nazwa_pliku,tab,b_polnocny,b_poludniowy,czas);
	for(int j=1;j<ilosc_wywolan;++j)
	{
		//if( j%10 == 0 )wspolcz-=1;

		//if( j%zapis_co_n == 0 )zapisuj_temperature_srednio_i_arg_wywolania("WYNIKI\\plik_do_wykresow.txt",tab,czas,j);
		//if( j%zapis_co_n == 0 )zapisuj_temperature_srednio_i_arg_wywolania("WYNIKI\\wykresy.txt",tab,czas,j);
		if( j%100 == 0 ){ cout<< "<status>" << j*100/ilosc_wywolan <<  "\%</status>\n"; }
		akcja_w_godz(tab,b_polnocny,b_poludniowy,czas,1);
	}
	zapisuj_temperature_srednio_i_arg_wywolania("WYNIKI\\temp_od_wsp_reemisji.txt",tab,czas,0);
	}




	cout<<czas.rok_dzien_godzina_minuta()<<endl;
	cout<<"temperatura minimalna: \t"<<"<min_temp>"<<tab.temperatura_min_max().first<<"</min_temp>"<<endl;
	cout<<"temperatura maksymalna:\t"<<"<max_temp>"<<tab.temperatura_min_max().second<<"</max_temp>"<<endl;
	cout<<"srednia temperatura:   \t"<<"<avr_temp>"<<tab.srednia_temperatura()<<"</avr_temp>" << endl;
	cout<<"srednie albedo:        \t"<<"<avr_albe>"<<tab.srednie_albedo()<<"</avr_albe>" << endl;
	
	

	//zapisz(nazwa_pliku,tab,b_polnocny,b_poludniowy,czas);
	rysuj_ziemie_jako_jajko("temperatura_0.txt",tab);
	//zapisuj_temperature_srednio_i_arg_wywolania("WYNIKI\\temp_od_wsp_reemisji.txt",tab,czas,0);



	//PLIKI
	/*
	"temperatura_0.txt" - mapa temperatur
	"plik_do_wykresow.txt" - zapisuje dane do wykresów
	"swiat.txt" - do zczytywania mapy œwiata
	"plik_zapisu.txt" - zapamientuje stan ostatniej symulacji
	"test.czytania_swiata.txt" - sprawdza czy mapa œwiata dobrze siê wczyta³a
	"zapis_czasu.txt" - zapis czasu (do funkci s³oñce) ostatniej symulacji
	*/
}
