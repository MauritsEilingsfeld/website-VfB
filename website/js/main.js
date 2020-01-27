let alle_bundesliga_ergebnisse = null


fetch('https://www.openligadb.de/api/getmatchdata/bl2/2019')
    .then((response) => {
        return response.json();
    })
    .then((myJson) => {
        alle_bundesliga_ergebnisse = myJson
        console.log(alle_bundesliga_ergebnisse);
        abruf_der_spiele()
    });


function bestimme_endergebnis_aus_liste_mit_toren(aktuelleListeMitAllentoren) {
    aktuelleListeMitAllentoren.forEach((aktuelles_einzelnes_tor) => {
        Tore_team1 = aktuelles_einzelnes_tor['ScoreTeam1']
        Tore_team2 = aktuelles_einzelnes_tor['ScoreTeam2']
        ScoreTeam1 = (Tore_team1, Tore_team2)
    })
    return ScoreTeam1
}

function bestimme_namen_beider_teams(spiel) {
    team_name1 = spiel['Team1']['TeamName']
    team_name2 = spiel['Team2']['TeamName']
    return {
        first: team_name1,
        second: team_name2
    }

}

function abruf_der_spiele() {
    alle_bundesliga_ergebnisse.forEach((spiel) => {
        einzelnes_spiel = alle_bundesliga_ergebnisse[0]
        aktuelle_matchid = einzelnes_spiel['MatchID']

        aktuelle_spielergebnisse = einzelnes_spiel['MatchResults']
        console.log(aktuelle_spielergebnisse);
        endergebnis = aktuelle_spielergebnisse[0]

        team1 = bestimme_namen_beider_teams(einzelnes_spiel)
        team2 = bestimme_namen_beider_teams(einzelnes_spiel)

        ergebnisbeschreibung = endergebnis['ResultDescription']

        punkte_team1 = endergebnis['PointsTeam1']
        punkte_team2 = endergebnis['PointsTeam2']

        aktuelles_Torverhältnis = einzelnes_spiel['Goals']

        Torverhältnis = aktuelles_Torverhältnis
        alle_aktuellen_tore_als_liste = aktuelles_Torverhältnis

        tor1 = Torverhältnis[0]
        Tore_team1 = tor1['ScoreTeam1']
        Tore_team2 = Torverhältnis[0]['ScoreTeam2']

        ScoreTeam1 = (Tore_team1, Tore_team2)



        spielendergebnis = bestimme_endergebnis_aus_liste_mit_toren(alle_aktuellen_tore_als_liste)

        zaehler_fuer_siege = 0

        zaehler_fuer_Unentschieden = 0

        zaehler_fuer_niederlagen = 0

        zaehler_fuer_tore_von_vfb = 0



        zaehler_fuer_gewonnene_spiele = 0

        zaehler_fuer_Unentschiede_spiele = 0

        zaehler_fuer_verlorene_spiele = 0

        zaehler_fuer_vfb_spiele = 0

        tor = {}

        // spiel.forEach((alle_bundesliga_ergebnisse) => {

        team1_tore = 0
        team2_tore = 0

        let spiel_tor_liste = null

        let o = bestimme_namen_beider_teams(spiel)
        team1 = o.first
        team2 = o.second
        if (team1 == "VfB Stuttgart" || team2 == "VfB stuttgart") {
            console.log(team1 + " Spielt gegen " + team2)

            spiel_tor_liste = spiel['Goals']


            zeitpunkt_des_spiels = spiel['MatchDateTime']
            aktuelles_Datum = "2020-01-23T08:30:00"
            if (aktuelles_Datum < zeitpunkt_des_spiels) {
                console.log("Das Spiel wurde noch nicht gespielt");
            } else console.log("Das Spiel hat am " + zeitpunkt_des_spiels + " stattgefunden.");
            if (spiel_tor_liste.length == 0) {
                console.log("Spiel ist 0:0 ausgegangen.");
            } else {
                erstes_geschossenes_tor = spiel_tor_liste[0]
                console.log(erstes_geschossenes_tor);
            }

            team1 = bestimme_namen_beider_teams(spiel)
            team2 = bestimme_namen_beider_teams(spiel)

            spiel_tor_liste.forEach((tor) => {
                console.log("Ein Tor ist gefallen")
                team1_tore = tor['ScoreTeam1']
                team2_tore = tor['ScoreTeam2']
                console.log('H: ' + (team1_tore))
                console.log('A: ' + (team2_tore))
            })

            let liste_mit_spielergebnissen = spiel['MatchResults']
            console.log(liste_mit_spielergebnissen)
            endspielergebnis = liste_mit_spielergebnissen
            console.log(endergebnis)
            PointsTeam1 = endspielergebnis['PointsTeam1']
            PointsTeam2 = endspielergebnis['PointsTeam2']
            if (team1 == "VfB Stuttgart" || team2 == "VfB Stuttgart"){
            console.log("Heim:" + PointsTeam1 + " Auswerts:" + PointsTeam2)
            spiel_tor_liste = spiel['Goals']
            console.log(spiel_tor_liste)
            spiel_tor_liste = spiel['Goals']
            console.log("Liste mit Toren aus dem Spiel" + spiel_tor_liste)
            }

            if (team1_tore > team2_tore){
                 if (team1 == "VfB Stuttgart")
                 console.log("VfB Tore bei Sieg:" + team1_tore)
                 zaehler_fuer_siege = zaehler_fuer_siege + team1_tore
 
                 zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + team1_tore
                 console.log("Tore Insgesamt:" + zaehler_fuer_tore_von_vfb)
            }

            if (team1_tore < team2_tore){
                 if (team2 == "VfB Stuttgart")
                 console.log("VfB Tore bei Sieg:" + team2_tore)
                 zaehler_fuer_siege = zaehler_fuer_siege + team2_tore

                 zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + team2_tore
                 console.log("Tore Insgesamt:" + zaehler_fuer_tore_von_vfb)
            }





            if (team1_tore == team2_tore){
                 if (team2 == "VfB Stuttgart")
                 console.log("VfB Tore bei Unentschieden:" + team1_tore)
                 zaehler_fuer_siege = zaehler_fuer_Unentschieden + team1_tore
            }

                 zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + team1_tore
                 console.log("Tore Insgesamt:" + zaehler_fuer_tore_von_vfb)

            if (team1_tore == team2_tore){
                 if (team1 == "VfB Stuttgart")
                 console.log("VfB Tore bei Unentschieden:" + team2_tore)
                 zaehler_fuer_siege = zaehler_fuer_Unentschieden + team2_tore

                 zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + team2_tore
                  console.log("Tore Insgesamt:" + zaehler_fuer_tore_von_vfb)
            }



            if (team1_tore < team2_tore){
                 if (team1 == "VfB Stuttgart")
                 console.log("VfB Tore bei Niederlage:" + team1_tore)
                 zaehler_fuer_niederlagen = zaehler_fuer_niederlagen + team1_tore

                 zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + team1_tore
                 console.log("Tore Insgesamt:" + zaehler_fuer_tore_von_vfb)
            }

            if (team1_tore > team2_tore){
                 if (team2 == "VfB Stuttgart")
                 console.log("VfB Tore bei Niederlage:" + team2_tore)
                 zaehler_fuer_niederlagen = zaehler_fuer_niederlagen + team2_tore
 
                 zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + team2_tore
                console.log("Tore Insgesamt:" + zaehler_fuer_tore_von_vfb)
            }



            if (team1_tore > team2_tore){
                 if (team1 == "VfB Stuttgart")
                 console.log("VfB hat gewonnen")
                 zaehler_fuer_gewonnene_spiele = zaehler_fuer_gewonnene_spiele + 3
                 console.log("Gewonnene Spiele:" + zaehler_fuer_gewonnene_spiele)
            }

            if (team1_tore < team2_tore){
                 if (team1 == "VfB Stuttgart")
                 console.log("VfB hat gewonnen")
                 zaehler_fuer_gewonnene_spiele = zaehler_fuer_gewonnene_spiele + 3
                 console.log("Gewonnene Spiele:" + zaehler_fuer_gewonnene_spiele)
            }



            if (team1_tore == team2_tore){
                 if (team1 == "VfB Stuttgart")
                 console.log("VfB hat Unentschieden gespielt")
                 zaehler_fuer_Unentschiede_spiele = zaehler_fuer_Unentschiede_spiele + 1
                 console.log("Unentschiedene Spiele:" + zaehler_fuer_Unentschiede_spiele)
            }

            if (team1_tore == team2_tore){
                 if (team2 == "VfB Stuttgart")
                 console.log("VfB hat Unentschieden gespielt")
                 zaehler_fuer_Unentschiede_spiele = zaehler_fuer_Unentschiede_spiele + 1
                 console.log("Unentschiedene Spiele:" + zaehler_fuer_Unentschiede_spiele)
            }
        



            if (team1_tore < team2_tore){
                 if (team1 == "VfB Stuttgart")
                 console.log("VfB hat verloren")
                 zaehler_fuer_verlorene_spiele = zaehler_fuer_verlorene_spiele + 1
                 console.log("Verlorene Spiele:" + zaehler_fuer_verlorene_spiele)
            }

            if (team1_tore > team2_tore){
                 if (team2 == "VfB Stuttgart")
                 console.log("VfB hat verloren")
                 zaehler_fuer_verlorene_spiele = zaehler_fuer_verlorene_spiele + 1
                 console.log("Verlorene Spiele:" + zaehler_fuer_verlorene_spiele)
            }




            if (team1 == "VfB Stuttgart" || team2 == "VfB Stuttgart"){
            zaehler_fuer_vfb_spiele = zaehler_fuer_vfb_spiele + 1
            }
            console.log("Gespielte Partien:" + zaehler_fuer_vfb_spiele)
            console.log()
        }
    })

}








