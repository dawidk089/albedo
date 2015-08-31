
using namespace std;

//#pragma once

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <ostream>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <utility>
#include <ctime>
#include <stdio.h>
#include <functional>
#include <stdlib.h>


extern int ilosc_poludnikow;
extern int ilosc_rownoleznikow;
extern double promien_ziemi;
extern double pi;
extern double szerokosc_kontowa_biegunow_przez_2;
extern double stala_sloneczna;
extern double stala_Stefana_Boltzmana;
extern double wspulczynnik_reemisji;//globalne ocieplenie
extern double wsp_dyf;
extern int fun_slonce;
extern int fun_emisja;
extern int fun_wymiana_ciepla;
extern double albedo_parametr_lad;
extern double albedo_parametr_morze;
extern int albedo_rodzaj;
extern int ilosc_wywolan;
extern double cieplo_wlasciwe_lad;
extern double cieplo_wlasciwe_morze;
extern int czyt_mape_swiata;
extern int aargc;
extern char ** aargv;
//////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*
Spis tresci (kolejnosc definicji deklaracji klas/funkcji/stalych globalnych w kodzie:
	1)stale globalne-tylko w Projekt_FS.cpp
klasy:
	2)Czas
	3)Pole
	4)Tablica_Pol
	5)funkcje albedo
	6)zwykle fumkcje
	7)klasa wektor
*/
//////////////////////////////////////////////////////////////////////////////////////////////////////////////





class Czas
{
private:
	double dni_w_roku;
	//double minuta;
	double godzina;//godzina roku/////// 24*365.25=ilosc godzin w roku
	double doba;
	double kat_odchylenia;//k¹t odchylenia osi obrotu wok³o³ w³asnej osi od p³aszcztzny obiegu

public:
	Czas();
	double kat_dobowy(); //zwraca k¹t obrotu ziemi w ci¹gu doby
	double kat_roczny(); //zwraca k¹t obrotu ziemi w ci¹gu roku
	void zwieksz_godzine();
	void zwieksz_minute();
	string rok_dzien_godzina_minuta();


	double& ref_dni_w_roku();
	double& ref_godzina();
	double& ref_doba();
	double& ref_kat_odchylenia();
};




class Pole
{
private:
	int nr_poludnik;
	int nr_rownoleznik;
	double cieplo_wlasciwe;
	double wspulczynnik_dyfuzji;
	double energia_wew;
	double dlugosc_poludnikowa;
	double dlugosc_rownoleznikowa;
	double pole_powiezchni;
	int rodz_powierzchni;
	

public:
	Pole();
	Pole(int nr_poludnik, int nr_rownoleznik, double albedo, double cieplo_wlasciwe, double wspulczynnik_dyfuzji,double energia_wew,int rodz_powierzchni);
	Pole(const Pole& );
	void zmien(int nr_poludnik, int nr_rownoleznik, double albedo, double cieplo_wlasciwe, double wspulczynnik_dyfuzji,double energia_wew,int rodz_powierzchni);

double poludnik();

double rownoleznik();

double temperatura();
 
double albedo_od_T();

double C_wlasciwe();

int& ref_nr_poludnik();
int& ref_nr_rownoleznik();
double& ref_dlugosc_poludnikowa();
double& ref_dlugosc_rownoleznikowa();
double& ref_pole_powiezchni();
double& ref_albedo();
double& ref_cieplo_wlasciwe();
double& ref_wspulczynnik_dyfuzji();
double& ref_energia_wew();
int& ref_rodz_powierzchni();

};




class Tablica_Pol
{
public:
	vector <vector <Pole> > tab_pol_row; /////kolejnosc wspolzendnych geograficznych jak w matematyce (x,y) ----> [poludnik][rownoleznik]


	Tablica_Pol();
	double srednia_temperatura();

};


void slonce_w_min(Tablica_Pol& tab,Pole& b_polnocny,Pole& b_poludniowy, Czas& czas);
void emisja_w_min(Tablica_Pol& tab,Pole& b_polnocny,Pole& b_poludniowy);
void wymiana_ciepla_w_min(Tablica_Pol& tab,Pole& b_polnocny,Pole& b_poludniowy);
void akcja_w_min(Tablica_Pol& tab,Pole& b_polnocny,Pole& b_poludniowy, Czas& czas, int ilosc_wywolan);

void slonce_w_godz(Tablica_Pol& tab,Pole& b_polnocny,Pole& b_poludniowy, Czas& czas);
void emisja_w_godz(Tablica_Pol& tab,Pole& b_polnocny,Pole& b_poludniowy);
void wymiana_ciepla_w_godz(Tablica_Pol& tab,Pole& b_polnocny,Pole& b_poludniowy);
void akcja_w_godz(Tablica_Pol& tab,Pole& b_polnocny,Pole& b_poludniowy, Czas& czas, int ilosc_wywolan);

bool zapisz(const string,Tablica_Pol&,const Pole&,const Pole&);
bool czytaj(const string,Tablica_Pol&,const Pole&,const Pole&);
bool rysuj_ziemie_jako_jajko(const string,Tablica_Pol&);
bool czytaj_mape_swiata(const string,Tablica_Pol&);
bool zapisuj_temperature_srednio_i_arg_wywolania(const string,Tablica_Pol&);

class wektor
{
private:
	double x;
	double y;
	double z;
public:
	wektor (double ,double ,double );
	double operator* (wektor);
	
};


