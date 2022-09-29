public class TemaCurs0 {
/*
exercitiul 1. o variabila = o zona din memoria unui calculator care tine diferite date, o cutiuta in care noi punem valori
boolean = se refera la tipul de date care ii este atribuit variabilei false sau true,adica ocupa doar un bit,
 o singura valoare:false=0 iar true=1.
 */

    //exercitiul 3. declarare si initializare variabila string(sir de caractere de la tastatura)
    public static void main(String[] args) {
        String tipApartament="garsoniera";
        System.out.println("Apartamentul este de tip"+" " + tipApartament);

        //declarare si initializare variabila integer(numar intreg)
        Integer numarCamere= 2;
        System.out.println("Apartamentul are"+" "+numarCamere+" "+"camere");

        //declaram si initializam o variabila double
        Double pretApartament= 65000.50;
        System.out.println("Pretul apartamentului este de" + " " + pretApartament+ " " + "euro");

        //declaram si initializam o variabila boolean
        boolean dezvoltator= false;
        boolean autorizatie_constructie= true;
        System.out.println("Daca dezvoltatorul este"+" "+ dezvoltator + " "+ "atunci nu cumpar");
        System.out.println("Cumpar apartamentul daca are autorizatie constructie"+ " " + autorizatie_constructie );


        //exercitiul 5

        //reprezinta executaree unui cod intr-o lupa,care porneste de la setarea variabilei la valoarea i=1,
        // se stabileste o conditie care se repeta atata timp cate ste adevarata pana la i<20
        //i=1, i = 1+3=4, i = 4+3=7, i=7+3=10, i=10+3-13, i=13+3=16,i=16+3=19

        int i;
        for (i=1; i<20; i=i+3)
            System.out.println(i);

    }
}
