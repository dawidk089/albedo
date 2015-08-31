#include "Projekt_FS.h"

 
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




//////////////////////////////////////////////////////////////////////////////////////////////////////////////


Czas::Czas():dni_w_roku(365.25),godzina(0),doba(24),kat_odchylenia(23/180*pi){}

double Czas::kat_dobowy() {return (2*pi*godzina/doba);}

double Czas::kat_roczny() {return (kat_odchylenia*sin(2*pi*(godzina+100*24)/(doba*dni_w_roku)));}

void Czas::zwieksz_godzine() {++godzina;}
void Czas::zwieksz_minute() {godzina += (1./60.);}

string Czas::rok_dzien_godzina_minuta()
{
	string zwrot,tmp;
	stringstream xxx;
	double rok,dz,godz,min;
	rok=int(godzina/dni_w_roku/doba);
	dz=int((godzina-rok*dni_w_roku*doba)/doba);
	godz=int(godzina-rok*dni_w_roku*doba-doba*dz)+12;
	min=int(60*(godzina-int(godzina)));


	xxx<< "rok: "<<"<year>"<<rok<<"</year>"<<" dzien roku: "<<"<day>"<<dz<<"</day>"<<" godzina: "<<"<time>"<<godz<<":"<<min<<"</time>"<< endl;
	for(int i=0;i<7;++i){xxx>>tmp;zwrot+=tmp;zwrot+=" ";}
	zwrot+='\n';

	return zwrot;

}

double& Czas::ref_dni_w_roku(){ return dni_w_roku;}
double& Czas::ref_godzina(){ return godzina;}
double& Czas::ref_doba(){ return doba;}
double& Czas::ref_kat_odchylenia(){ return kat_odchylenia;}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////


Pole::Pole(){}



Pole::Pole(int nr_poludnik, int nr_rownoleznik, double albedo, double cieplo_wlasciwe, double wspulczynnik_dyfuzji,double energia_wew,int rodz_powierzchni):
nr_poludnik(nr_poludnik),
nr_rownoleznik(nr_rownoleznik),
cieplo_wlasciwe(cieplo_wlasciwe),
wspulczynnik_dyfuzji(wspulczynnik_dyfuzji),
energia_wew(energia_wew),
rodz_powierzchni(rodz_powierzchni)

{
	
	dlugosc_poludnikowa=abs(((pi-szerokosc_kontowa_biegunow_przez_2*2)*promien_ziemi)/ilosc_poludnikow);
	dlugosc_rownoleznikowa=abs((2*pi*sin( rownoleznik() )*promien_ziemi)/ilosc_rownoleznikow);
	pole_powiezchni=dlugosc_poludnikowa*dlugosc_rownoleznikowa;
}


Pole::Pole(const Pole& p):
nr_poludnik(p.nr_poludnik),
nr_rownoleznik(p.nr_rownoleznik),
cieplo_wlasciwe(p.cieplo_wlasciwe),
wspulczynnik_dyfuzji(p.wspulczynnik_dyfuzji),
energia_wew(p.energia_wew),
dlugosc_poludnikowa(p.dlugosc_poludnikowa),
dlugosc_rownoleznikowa(p.dlugosc_rownoleznikowa),
pole_powiezchni(p.pole_powiezchni),
rodz_powierzchni(p.rodz_powierzchni){}


void Pole::zmien(int nr_polu, int nr_rown, double albe, double ciep, double wspu,double ener,int rodz)
{
nr_poludnik=nr_polu;
nr_rownoleznik=nr_rown;
cieplo_wlasciwe=ciep;
wspulczynnik_dyfuzji=wspu;
energia_wew=ener;
rodz_powierzchni=rodz;
}


double Pole::poludnik()
{
	return (nr_poludnik+0.5)/(ilosc_poludnikow-1)*2*pi;

}


double Pole::rownoleznik()
{
	return (nr_rownoleznik+0.5)*(pi-2*szerokosc_kontowa_biegunow_przez_2)/ilosc_rownoleznikow+szerokosc_kontowa_biegunow_przez_2;

}

double Pole::temperatura()
{
	return energia_wew/C_wlasciwe()/pole_powiezchni;

}




//unikanie  :public    ---funkcje z referencjami

int& Pole::ref_nr_poludnik(){return  nr_poludnik ;}
int& Pole::ref_nr_rownoleznik(){return  nr_rownoleznik ;}
double& Pole::ref_dlugosc_poludnikowa(){return dlugosc_poludnikowa  ;}
double& Pole::ref_dlugosc_rownoleznikowa(){return dlugosc_rownoleznikowa  ;}
double& Pole::ref_pole_powiezchni(){return pole_powiezchni  ;}
double& Pole::ref_cieplo_wlasciwe(){return cieplo_wlasciwe  ;}
double& Pole::ref_wspulczynnik_dyfuzji(){return  wspulczynnik_dyfuzji ;}
double& Pole::ref_energia_wew(){return energia_wew  ;}
int& Pole::ref_rodz_powierzchni(){return rodz_powierzchni;}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Tablica_Pol::Tablica_Pol()
{
	tab_pol_row= vector<vector<Pole> >(ilosc_poludnikow);
	for(int i=0;i<ilosc_poludnikow;++i)
	{
		tab_pol_row[i]=vector<Pole>(ilosc_rownoleznikow);
		for(int j=0;j<ilosc_rownoleznikow;++j)
		{
			Pole p(i,j,0.31,cieplo_wlasciwe_morze,wsp_dyf,300,0);
			p.zmien(i,j,0.31,cieplo_wlasciwe_morze,wsp_dyf,300*p.ref_cieplo_wlasciwe()*p.ref_pole_powiezchni(),0);
			tab_pol_row[i][j]=p;

		}

	}

}

double Tablica_Pol::srednia_temperatura()
{
	double suma=0;
	for(int i=0;i<ilosc_poludnikow;++i)	
		for(int j=0;j<ilosc_rownoleznikow;++j)
			suma+=tab_pol_row[i][j].temperatura();

	return suma/ilosc_poludnikow/ilosc_rownoleznikow;
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
double Pole::albedo_od_T()
{
	switch(albedo_rodzaj)
	{
	case 1:
	{
		if(rodz_powierzchni==0)
		{
			if(temperatura()<(268))	return 0.85;
			else if(temperatura()<278) return ((temperatura()-268)*0.07+0.85);
			else return 0.15;
		}
		else
		{
			if(temperatura()<(268))	return 0.85;
			else if(temperatura()<278) return ((temperatura()-268)*0.055+0.85);
			else return 0.4;
		}
	}
	case 0:
			if(rodz_powierzchni==0)
				return albedo_parametr_morze;
			else 
				return albedo_parametr_lad;
		
	default: return albedo_parametr_lad;	
	} 
	
}

double Pole::C_wlasciwe()
{
	if(rodz_powierzchni==0)
		return cieplo_wlasciwe_morze;
	else
		return cieplo_wlasciwe_lad;
}


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////








void slonce_w_min(Tablica_Pol& tab,Pole& b_polnocny,Pole& b_poludniowy, Czas& czas)
{

	double il_skal;
	for(int j=0;j<ilosc_rownoleznikow;++j)
	{
		for(int i=0;i<ilosc_poludnikow;++i)
		{
				wektor n(-sin(tab.tab_pol_row[i][j].rownoleznik())*cos(tab.tab_pol_row[i][j].poludnik()),-sin(tab.tab_pol_row[i][j].rownoleznik())*sin(tab.tab_pol_row[i][j].poludnik()),-cos(tab.tab_pol_row[i][j].rownoleznik())),
				s(cos(czas.kat_roczny())*cos(czas.kat_dobowy()),cos(czas.kat_roczny())*sin(czas.kat_dobowy()),sin(czas.kat_roczny()));
				il_skal= n*s;
				
				if(il_skal>0)
				{	
					double dE=stala_sloneczna*tab.tab_pol_row[i][j].ref_pole_powiezchni()*il_skal*60*
					(1-tab.tab_pol_row[i][j].albedo_od_T());

					tab.tab_pol_row[i][j].ref_energia_wew() +=dE;
				}

			

		}

	}
	if(czas.kat_roczny()<0)
	b_polnocny.ref_energia_wew()+=stala_sloneczna*b_polnocny.ref_pole_powiezchni()*(-1)*sin(czas.kat_roczny())*60*(1-b_polnocny.albedo_od_T());
	else b_poludniowy.ref_energia_wew()+=stala_sloneczna*b_poludniowy.ref_pole_powiezchni()*(-1)*sin(czas.kat_roczny())*60*(1-b_poludniowy.albedo_od_T());	

}

void slonce_w_godz(Tablica_Pol& tab,Pole& b_polnocny,Pole& b_poludniowy, Czas& czas)
{

	double il_skal;
	for(int j=0;j<ilosc_rownoleznikow;++j)
	{
		for(int i=0;i<ilosc_poludnikow;++i)
		{
				wektor n(-sin(tab.tab_pol_row[i][j].rownoleznik())*cos(tab.tab_pol_row[i][j].poludnik()),-sin(tab.tab_pol_row[i][j].rownoleznik())*sin(tab.tab_pol_row[i][j].poludnik()),-cos(tab.tab_pol_row[i][j].rownoleznik())),
				s(cos(czas.kat_roczny())*cos(czas.kat_dobowy()),cos(czas.kat_roczny())*sin(czas.kat_dobowy()),sin(czas.kat_roczny()));
				il_skal= n*s;
				
				if(il_skal>0)
				{	
					double dE=stala_sloneczna*tab.tab_pol_row[i][j].ref_pole_powiezchni()*il_skal*3600*
					(1-tab.tab_pol_row[i][j].albedo_od_T());

					tab.tab_pol_row[i][j].ref_energia_wew() +=dE;
				}

			

		}

	}		
	if(czas.kat_roczny()<0)
	b_polnocny.ref_energia_wew()+=stala_sloneczna*b_polnocny.ref_pole_powiezchni()*(-1)*sin(czas.kat_roczny())*3600*(1-b_polnocny.albedo_od_T());
	else b_poludniowy.ref_energia_wew()+=stala_sloneczna*b_poludniowy.ref_pole_powiezchni()*(-1)*sin(czas.kat_roczny())*3600*(1-b_poludniowy.albedo_od_T());
}



void emisja_w_min(Tablica_Pol& tab,Pole& b_polnocny,Pole& b_poludniowy)
{
	double dE=0;
	Pole pole_test;
	for(int i=0;i<ilosc_poludnikow;++i)
	{
		for(int j=0;j<ilosc_rownoleznikow;++j)
		{
			dE=stala_Stefana_Boltzmana*tab.tab_pol_row[i][j].ref_pole_powiezchni()*pow((tab.tab_pol_row[i][j].temperatura()),4)*60*(1-wspulczynnik_reemisji);
			pole_test=tab.tab_pol_row[i][j];

 			if(pole_test.ref_energia_wew()-dE>0)	
				dE*=-1;
			else cout<<endl<<"uwaga ujemna temperatura BLAD!!!"<<endl;


			tab.tab_pol_row[i][j].ref_energia_wew()+=dE;
		}

	}
	b_polnocny.ref_energia_wew()-=stala_Stefana_Boltzmana*b_polnocny.ref_pole_powiezchni()*pow((b_polnocny.temperatura()),4)*60*(1-wspulczynnik_reemisji);
	b_poludniowy.ref_energia_wew()-=stala_Stefana_Boltzmana*b_poludniowy.ref_pole_powiezchni()*pow((b_poludniowy.temperatura()),4)*60*(1-wspulczynnik_reemisji);

}

void emisja_w_godz(Tablica_Pol& tab,Pole& b_polnocny,Pole& b_poludniowy)
{
	double dE=0;
	Pole pole_test;
	for(int i=0;i<ilosc_poludnikow;++i)
	{
		for(int j=0;j<ilosc_rownoleznikow;++j)
		{
			dE=stala_Stefana_Boltzmana*tab.tab_pol_row[i][j].ref_pole_powiezchni()*pow((tab.tab_pol_row[i][j].temperatura()),4)*3600*(1-wspulczynnik_reemisji);
			pole_test=tab.tab_pol_row[i][j];

 			if(pole_test.ref_energia_wew()-dE>0)	
				dE*=-1;
			else cout<<endl<<"uwaga ujemna temperatura BLAD!!!"<<endl;


			tab.tab_pol_row[i][j].ref_energia_wew()+=dE;
		}

	}
	b_polnocny.ref_energia_wew()-=stala_Stefana_Boltzmana*b_polnocny.ref_pole_powiezchni()*pow((b_polnocny.temperatura()),4)*3600*(1-wspulczynnik_reemisji);
	b_poludniowy.ref_energia_wew()-=stala_Stefana_Boltzmana*b_poludniowy.ref_pole_powiezchni()*pow((b_poludniowy.temperatura()),4)*3600*(1-wspulczynnik_reemisji);	

}










void akcja_w_min(Tablica_Pol& tab,Pole& b_polnocny,Pole& b_poludniowy, Czas& czas, int ilosc_wywolan)
{
	for(int i=0;i<ilosc_wywolan;++i)
	{
		if(fun_slonce)slonce_w_min(tab,b_polnocny,b_poludniowy,czas);
		if(fun_emisja)emisja_w_min(tab,b_polnocny,b_poludniowy);
		if(fun_wymiana_ciepla)wymiana_ciepla_w_min(tab,b_polnocny,b_poludniowy);
		czas.zwieksz_minute();



	}
}

void akcja_w_godz(Tablica_Pol& tab,Pole& b_polnocny,Pole& b_poludniowy, Czas& czas, int ilosc_wywolan)
{
	for(int i=0;i<ilosc_wywolan;++i)
	{
		if(fun_slonce)slonce_w_godz(tab,b_polnocny,b_poludniowy,czas);
		if(fun_emisja)emisja_w_godz(tab,b_polnocny,b_poludniowy);
		if(fun_wymiana_ciepla)wymiana_ciepla_w_godz(tab,b_polnocny,b_poludniowy);
		czas.zwieksz_godzine();


	}
}




// funkcje zapisz i czytaj

bool zapisz(const string nazwa_pliku,Tablica_Pol& tab,const Pole& bieg_polu,const Pole& bieg_poln)
{
	ofstream plik;
	plik.open(nazwa_pliku.c_str());
	if( !plik.good() ){cout<<endl<<"blad otwarcia pliku w funkcji zapis"<<endl;return false;}
	
	
	for(int i=0;i<ilosc_poludnikow;++i)
	{
		for(int j=0;j<ilosc_rownoleznikow;++j)
		{
			plik<<"x"<<" "<<         ////////'x'-ozancza rozpoczecie zapisu nastepnego pola
			tab.tab_pol_row[i][j].poludnik()<<" "<<
			tab.tab_pol_row[i][j].rownoleznik()<<" "<<
			tab.tab_pol_row[i][j].temperatura()<<" "<<
			tab.tab_pol_row[i][j].ref_nr_poludnik()<<" "<<
			tab.tab_pol_row[i][j].ref_nr_rownoleznik()<<" "<<
			tab.tab_pol_row[i][j].ref_dlugosc_poludnikowa()<<" "<<
			tab.tab_pol_row[i][j].ref_dlugosc_rownoleznikowa()<<" "<<
			tab.tab_pol_row[i][j].ref_pole_powiezchni()<<" "<<
			tab.tab_pol_row[i][j].albedo_od_T()<<" "<<
			tab.tab_pol_row[i][j].ref_cieplo_wlasciwe()<<" "<<
			tab.tab_pol_row[i][j].ref_wspulczynnik_dyfuzji()<<" "<<
			tab.tab_pol_row[i][j].ref_energia_wew()<<" ";
		}
		plik<<endl;
	}
	plik.close();
	return true;


/*   Kolejnoœæ zapisu danych do pliku jak ponizej
double poludnik();
double rownoleznik();
double temperatura();
int& ref_nr_poludnik();
int& ref_nr_rownoleznik();
double& ref_dlugosc_poludnikowa();
double& ref_dlugosc_rownoleznikowa();
double& ref_pole_powiezchni();
double albedo_od_T();
double& ref_cieplo_wlasciwe();
double& ref_wspulczynnik_dyfuzji();
double& ref_energia_wew();
*/
}






bool czytaj(const string nazwa_pliku,Tablica_Pol& tab,const Pole& bieg_polu,const Pole& bieg_poln)
{
	ifstream plik;
	plik.open(nazwa_pliku.c_str());
	if( !plik.good() ){cout<<endl<<"blad otwarcia pliku w funkcji czytaj"<<endl;return false;}
	
	
	for(int i=0;i<ilosc_poludnikow;++i)
	{
		for(int j=0;j<ilosc_rownoleznikow;++j)
		{
			if(plik.good()){
			char c,smiec;
			plik>>c;
			while(c=='x')
			{
				plik>>smiec;
				plik>>smiec;
				plik>>smiec;
				plik>>smiec;
				plik>>tab.tab_pol_row[i][j].ref_nr_poludnik();
				plik>>tab.tab_pol_row[i][j].ref_nr_rownoleznik();
				plik>>tab.tab_pol_row[i][j].ref_dlugosc_poludnikowa();
				plik>>tab.tab_pol_row[i][j].ref_dlugosc_rownoleznikowa();
				plik>>tab.tab_pol_row[i][j].ref_pole_powiezchni();
				plik>>tab.tab_pol_row[i][j].ref_cieplo_wlasciwe();
				plik>>tab.tab_pol_row[i][j].ref_wspulczynnik_dyfuzji();
				plik>>tab.tab_pol_row[i][j].ref_energia_wew();
				plik>>c;
			}}else cout<<endl<<"cos zlego stalo sie z plikiem przy czytania"<<endl;		
		}
	}
	plik.close();
	return true;

/*   Kolejnoœæ czytania danych do pliku jak ponizej
double poludnik();
double rownoleznik();
double temperatura();
int& ref_nr_poludnik();
int& ref_nr_rownoleznik();
double& ref_dlugosc_poludnikowa();
double& ref_dlugosc_rownoleznikowa();
double& ref_pole_powiezchni();
double& ref_cieplo_wlasciwe();
double& ref_wspulczynnik_dyfuzji();
double& ref_energia_wew();
*/
}


bool czytaj_mape_swiata(const string nazwa_pliku,Tablica_Pol& tab)
{
	ifstream plik;
	plik.open(nazwa_pliku.c_str());
	if( !plik.good() ){cout<<endl<<"blad otwarcia pliku w funkcji czytaj"<<endl;return false;}
	
	ofstream swiat;
	swiat.open("test.czytania_swiata.txt");
	if( !swiat.good() ){cout<<endl<<"blad otwarcia pliku "<<endl;return false;}

	int i=0;
	char c;string linia;
	for(int j=0;j<ilosc_rownoleznikow;++j)
	{
		getline(plik,linia);
		for(int l=0;l<linia.size();++l)
		{
			{
				c=linia[l];
				if(atoi(&c)==1||atoi(&c)==0)tab.tab_pol_row[i][j].ref_rodz_powierzchni()=atoi(&c);
				++i;
			}
			i=0;

		}
	}
	for(int i=0;i<ilosc_rownoleznikow;++i)
	{
		for(int j=0;j<ilosc_poludnikow;++j)
		{
			
			swiat<<tab.tab_pol_row[i][j].ref_rodz_powierzchni()<<" ";
		}
		swiat<<endl;
	}
	plik.close();
	swiat.close();
	return true;


}



bool rysuj_ziemie_jako_jajko(const string nazwa_pliku,Tablica_Pol& tab)
{
	ofstream plik;double szerokosc_legendy=0.3;
	plik.open(nazwa_pliku.c_str());
	if( !plik.good() ){cout<<endl<<"blad otwarcia pliku w funkcji zapis"<<endl;return false;}
	
	double A=5*ilosc_poludnikow;
	for(int j=0;j<ilosc_rownoleznikow;++j)
	{
		for(int i=0;i<A;++i)
		{
			
			if(i>=(A/2*(1-sin(tab.tab_pol_row[int((i)/5.)][j].rownoleznik())))&&i<(A/2*(1+sin(tab.tab_pol_row[int(i/5.)][j].rownoleznik()))))
			{	
				int index=(i-A/2*(1-sin(tab.tab_pol_row[int(i/5.)][j].rownoleznik())))/5/sin(tab.tab_pol_row[int(i/5.)][j].rownoleznik());

				plik<<10*int(tab.tab_pol_row[index][j].temperatura()/10)<<" ";
			}
			//else if (i>A*(1-szerokosc_legendy)&&(j>ilosc_rownoleznikow*0.9&&j<ilosc_rownoleznikow*0.98))plik<<(i-A*(1-szerokosc_legendy)+1)*500./A/szerokosc_legendy<<" ";
			//else if (i>A*(1-szerokosc_legendy)&&(j>ilosc_rownoleznikow*0.98))plik<<300<<" ";
			else {plik<<0<<" ";}

		}
		plik<<endl;
	}


	plik.close();
	return true;


}

bool zapisuj_temperature_srednio_i_arg_wywolania(const string nazwa_pliku,Tablica_Pol& tab)
{
	ofstream plik;stringstream tmp;string tmp2;
	plik.open(nazwa_pliku.c_str(),ios::app);
	if( !plik.good() ){cout<<endl<<"blad otwarcia pliku"<<endl;return false;}
	else{ 
	

			/*plik<<tab.srednia_temperatura()<<" "<<stala_sloneczna<<" "<<wspulczynnik_reemisji<<" "<<stala_sloneczna<<" "<<wsp_dyf<<
			" "<<albedo_parametr_lad<<" "<<albedo_parametr_morze<<" "<<albedo_rodzaj<<" "<<ilosc_wywolan<<" "<<cieplo_wlasciwe_lad<<
			" "<<cieplo_wlasciwe_morze<<" "<<czyt_mape_swiata<<endl;  */  
			
			for(int i=1;i<aargc;++i)
			{
				plik<<atof(aargv[i])<<" ";
				cout<<"atof(aargv[i]): " <<atof(aargv[i])<<" ";										
			}
			plik<<tab.srednia_temperatura()<<" "; 
			plik<<endl;
		}
		/*while (tmp.good())tmp>>tmp2;
		int i=0;
		while(i<tmp2.size())
		{
			if(tmp2[i]=='.')
				plik<<',';
			else
				plik<<tmp2[i];
			++i;
		}*/	


	plik.close();
	return true;
}
/*if(argc>1)ilosc_poludnikow=atof(argv[1]);
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
if(argc>15)czyt_mape_swiata=atof(argv[15]);*/







//klasa wektor

wektor::wektor (double x,double y,double z){
	this->x=x;
	this->y=y;
	this->z=z;
}


double wektor::operator* (wektor b)
{
    wektor a=*this;
     return (a.x*b.x+a.y*b.y+a.z*b.z);
}






void wymiana_ciepla_w_min(Tablica_Pol& tab,Pole& b_polnocny,Pole& b_poludniowy)
{
	double wspulczynnik_dyfuzji=wsp_dyf;
	Tablica_Pol tmp;
	double dE,przekotna,dl_pol,dl_row;
	for(int i=0;i<ilosc_poludnikow;++i)
	for(int j=0;j<ilosc_rownoleznikow;++j)
		tmp.tab_pol_row[i][j]=tab.tab_pol_row[i][j];

	Pole tmp_b_polnocny(b_polnocny),tmp_b_poludniowy(b_poludniowy);
	for(int i=1;i<ilosc_poludnikow-1;++i)
		for(int j=1;j<ilosc_rownoleznikow-1;++j)
			{
				dl_pol=	tmp.tab_pol_row[i][j].ref_dlugosc_poludnikowa();
				dl_row= tmp.tab_pol_row[i][j].ref_dlugosc_rownoleznikowa();
				przekotna=sqrt(pow(dl_pol,2)+pow(dl_row,2));
				dE=(tmp.tab_pol_row[i-1][j+1].temperatura()-tmp.tab_pol_row[i][j].temperatura())/przekotna*wspulczynnik_dyfuzji*60;
					tab.tab_pol_row[i][j].ref_energia_wew()+=dE;tab.tab_pol_row[i-1][j+1].ref_energia_wew()-=dE;
				dE=(tmp.tab_pol_row[i][j+1].temperatura()-tmp.tab_pol_row[i][j].temperatura())/dl_row*wspulczynnik_dyfuzji*60;
					tab.tab_pol_row[i][j].ref_energia_wew()+=dE;tab.tab_pol_row[i][j+1].ref_energia_wew()-=dE;
				dE=(tmp.tab_pol_row[i+1][j+1].temperatura()-tmp.tab_pol_row[i][j].temperatura())/przekotna*wspulczynnik_dyfuzji*60;
					tab.tab_pol_row[i][j].ref_energia_wew()+=dE;tab.tab_pol_row[i+1][j+1].ref_energia_wew()-=dE;
				dE=(tmp.tab_pol_row[i-1][j].temperatura()-tmp.tab_pol_row[i][j].temperatura())/dl_row*wspulczynnik_dyfuzji*60;
					tab.tab_pol_row[i][j].ref_energia_wew()+=dE;tab.tab_pol_row[i-1][j].ref_energia_wew()-=dE;
				dE=(tmp.tab_pol_row[i+1][j].temperatura()-tmp.tab_pol_row[i][j].temperatura())/dl_row*wspulczynnik_dyfuzji*60;
					tab.tab_pol_row[i][j].ref_energia_wew()+=dE;tab.tab_pol_row[i+1][j].ref_energia_wew()-=dE;
				dE=(tmp.tab_pol_row[i-1][j-1].temperatura()-tmp.tab_pol_row[i][j].temperatura())/przekotna*wspulczynnik_dyfuzji*60;
					tab.tab_pol_row[i][j].ref_energia_wew()+=dE;tab.tab_pol_row[i-1][j-1].ref_energia_wew()-=dE;
				dE=(tmp.tab_pol_row[i][j-1].temperatura()-tmp.tab_pol_row[i][j].temperatura())/dl_row*wspulczynnik_dyfuzji*60;
					tab.tab_pol_row[i][j].ref_energia_wew()+=dE;tab.tab_pol_row[i][j-1].ref_energia_wew()-=dE;
				dE=(tmp.tab_pol_row[i+1][j-1].temperatura()-tmp.tab_pol_row[i][j].temperatura())/przekotna*wspulczynnik_dyfuzji*60;	
					tab.tab_pol_row[i][j].ref_energia_wew()+=dE;tab.tab_pol_row[i+1][j-1].ref_energia_wew()-=dE;
			}

			


}















void wymiana_ciepla_w_godz(Tablica_Pol& tab,Pole& b_polnocny,Pole& b_poludniowy)
{
	double wspulczynnik_dyfuzji=wsp_dyf;
	Tablica_Pol tmp;
	double dE,przekotna,dl_pol,dl_row;
	for(int i=0;i<ilosc_poludnikow;++i)
	for(int j=0;j<ilosc_rownoleznikow;++j)
		{tmp.tab_pol_row[i][j]=tab.tab_pol_row[i][j];}

	Pole tmp_b_polnocny(b_polnocny),tmp_b_poludniowy(b_poludniowy);
	for(int i=1;i<ilosc_poludnikow-1;++i)
		for(int j=1;j<ilosc_rownoleznikow-1;++j)
			{
				dl_pol=	tmp.tab_pol_row[i][j].ref_dlugosc_poludnikowa();
				dl_row= tmp.tab_pol_row[i][j].ref_dlugosc_rownoleznikowa();
				przekotna=sqrt(pow(dl_pol,2)+pow(dl_row,2));
				dE=(tmp.tab_pol_row[i-1][j+1].temperatura()-tmp.tab_pol_row[i][j].temperatura())/przekotna*wspulczynnik_dyfuzji*3600;
					tab.tab_pol_row[i][j].ref_energia_wew()+=dE;tab.tab_pol_row[i-1][j+1].ref_energia_wew()-=dE;
				dE=(tmp.tab_pol_row[i][j+1].temperatura()-tmp.tab_pol_row[i][j].temperatura())/dl_row*wspulczynnik_dyfuzji*3600;
					tab.tab_pol_row[i][j].ref_energia_wew()+=dE;tab.tab_pol_row[i][j+1].ref_energia_wew()-=dE;
				dE=(tmp.tab_pol_row[i+1][j+1].temperatura()-tmp.tab_pol_row[i][j].temperatura())/przekotna*wspulczynnik_dyfuzji*3600;
					tab.tab_pol_row[i][j].ref_energia_wew()+=dE;tab.tab_pol_row[i+1][j+1].ref_energia_wew()-=dE;
				dE=(tmp.tab_pol_row[i-1][j].temperatura()-tmp.tab_pol_row[i][j].temperatura())/dl_row*wspulczynnik_dyfuzji*3600;
					tab.tab_pol_row[i][j].ref_energia_wew()+=dE;tab.tab_pol_row[i-1][j].ref_energia_wew()-=dE;
				dE=(tmp.tab_pol_row[i+1][j].temperatura()-tmp.tab_pol_row[i][j].temperatura())/dl_row*wspulczynnik_dyfuzji*3600;
					tab.tab_pol_row[i][j].ref_energia_wew()+=dE;tab.tab_pol_row[i+1][j].ref_energia_wew()-=dE;
				dE=(tmp.tab_pol_row[i-1][j-1].temperatura()-tmp.tab_pol_row[i][j].temperatura())/przekotna*wspulczynnik_dyfuzji*3600;
					tab.tab_pol_row[i][j].ref_energia_wew()+=dE;tab.tab_pol_row[i-1][j-1].ref_energia_wew()-=dE;
				dE=(tmp.tab_pol_row[i][j-1].temperatura()-tmp.tab_pol_row[i][j].temperatura())/dl_row*wspulczynnik_dyfuzji*3600;
					tab.tab_pol_row[i][j].ref_energia_wew()+=dE;tab.tab_pol_row[i][j-1].ref_energia_wew()-=dE;
				dE=(tmp.tab_pol_row[i+1][j-1].temperatura()-tmp.tab_pol_row[i][j].temperatura())/przekotna*wspulczynnik_dyfuzji*3600;	
					tab.tab_pol_row[i][j].ref_energia_wew()+=dE;tab.tab_pol_row[i+1][j-1].ref_energia_wew()-=dE;
			}

			


}







