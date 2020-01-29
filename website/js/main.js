let alle_bundesliga_ergebnisse = null

let zaehler_fuer_siege = 0

let zaehler_fuer_Unentschieden = 0

let zaehler_fuer_niederlagen = 0

let zaehler_fuer_tore_von_vfb = 0



let zaehler_fuer_gewonnene_spiele = 0

let zaehler_fuer_Unentschiede_spiele = 0

let zaehler_fuer_verlorene_spiele = 0

let zaehler_fuer_vfb_spiele = 0

let spiele = []

function Spielresultate(spiel) {
    let MannschaftA = spiel['Team1']['TeamName']
    let MannschaftB = spiel['Team2']['TeamName']
    let resultat = null
    let spiel_tor_liste = spiel['Goals']
    let Tore_team1 = 0
    let Tore_team2 = 0

    if (spiel_tor_liste.length !== 0) {
        let Ergebnis = spiel_tor_liste[spiel_tor_liste.length - 1]
        Tore_team1 = Ergebnis['ScoreTeam1']
        Tore_team2 = Ergebnis['ScoreTeam2']
    }

    let team_name1 = spiel['Team1']['TeamName']
    let team_name2 = spiel['Team2']['TeamName']


    if (team1_tore > team2_tore) {
        if (team_name1 === "VfB Stuttgart") {
            resultat = "Sieg"
        }
    }

    if (team1_tore < team2_tore) {
        if (team_name2 === "VfB Stuttgart") {
            resultat = "Sieg"
        }
    }


    if (team1_tore === team2_tore) {
        if (team_name1 === "VfB Stuttgart") {
            resultat = "Unentschieden"
        }
    }

    if (team1_tore === team2_tore) {
        if (team_name2 === "VfB Stuttgart") {
            console.log("Unentschieden")
            resultat = "Unentschieden"
        }
    }

    if (team1_tore < team2_tore) {
        if (team_name1 === "VfB Stuttgart") {
            console.log("Niederlage")
            resultat = "Niederlage"
        }
    }

    if (team1_tore < team2_tore) {
        if (team_name1 === "VfB Stuttgart") {
            console.log("Niederlage")
            resultat = "Niederlage"
        }
    }


    return `<tr>
        <td>${MannschaftA}</td>
        <td>${MannschaftB}</td>
        <td>${Tore_team1}:${Tore_team2}</td>
        <td>${resultat}</td>
    </tr>
    `
}

function mache_tabelle() {
    let tabelle = `
    <tr>
        <th>Heimmannschaft</th>
        <th>Auswärtsmannschaft</th>
        <th>Ergebnis</th>
        <th>Resultat</th>
    </tr>
    `


    // über alle spiele iterieren
    spiele.forEach(spiel => {
        const row = Spielresultate(spiel)

        tabelle = tabelle + " " + row


    })

    let tabellenElement = document.getElementById("tabelle")
    console.log(tabelle)
    tabellenElement.innerHTML += tabelle



}

fetch('https://www.openligadb.de/api/getmatchdata/bl2/2019')
    .then((response) => {
        return response.json();
    })
    .then((myJson) => {
        alle_bundesliga_ergebnisse = myJson
        // console.log(alle_bundesliga_ergebnisse);

        abruf_der_spiele()
        console.log('\n')
        console.log("Tore bei Siegen:\t\t" + zaehler_fuer_siege)
        console.log("Tore bei Unentschieden:\t\t" + zaehler_fuer_Unentschieden)
        console.log("Tore bei niederlagen\t\t" + zaehler_fuer_niederlagen)
        console.log("Gesamtanzahl Tore:\t\t" + zaehler_fuer_tore_von_vfb)
        console.log('\n')
        console.log("Gespielte Partien:\t\t" + zaehler_fuer_vfb_spiele)
        console.log('\n')
        console.log("Punkte bei Siegen:\t\t" + zaehler_fuer_gewonnene_spiele)
        console.log("Punkte bei Unentschieden:\t" + zaehler_fuer_Unentschiede_spiele)
        console.log("Verlorene Spiele:\t\t" + zaehler_fuer_verlorene_spiele)
        ergebnis = zaehler_fuer_gewonnene_spiele + zaehler_fuer_Unentschiede_spiele
        console.log("Gesamtanzahl Punkte:\t\t" + ergebnis)
    })
    .then(() => {
        document.getElementById("ToreBeiSieg").innerHTML = zaehler_fuer_siege
        document.getElementById("ToreBeiUnentschieden").innerHTML = zaehler_fuer_Unentschieden
        document.getElementById("ToreBeiNiederlagen").innerHTML = zaehler_fuer_niederlagen
        document.getElementById("ToreInsgesamt").innerHTML = zaehler_fuer_tore_von_vfb
        document.getElementById("PunkteBeiSiegen").innerHTML = zaehler_fuer_gewonnene_spiele
        document.getElementById("PunkteBiUnentschieden").innerHTML = zaehler_fuer_Unentschiede_spiele
        document.getElementById("PunkteInsgesamt").innerHTML = ergebnis
        console.log(spiele)
        mache_tabelle()
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
        // console.log(aktuelle_spielergebnisse);
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



        tor = {}

        // spiel.forEach((alle_bundesliga_ergebnisse) => {

        team1_tore = 0
        team2_tore = 0

        let spiel_tor_liste = null

        let o = bestimme_namen_beider_teams(spiel)
        team1 = o.first
        team2 = o.second
        if (team1 === "VfB Stuttgart" || team2 === "VfB Stuttgart") {
            console.log(team1 + " Spielt gegen " + team2)
            spiel_tor_liste = spiel['Goals']
            console.log(spiel_tor_liste)



            zeitpunkt_des_spiels = spiel['MatchDateTime']
            aktuelles_Datum = "2020-01-23T08:30:00"
            if (aktuelles_Datum < zeitpunkt_des_spiels) {
                console.log("Das Spiel wurde noch nicht gespielt");
            } else {
                spiele.push(spiel)
                console.log("Das Spiel hat am " + zeitpunkt_des_spiels + " stattgefunden.");
                if (spiel_tor_liste.length === 0) {
                    console.log("Spiel ist 0:0 ausgegangen.");
                } else {
                    erstes_geschossenes_tor = spiel_tor_liste[0]
                    console.log(erstes_geschossenes_tor);
                }



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
                if (team1 === "VfB Stuttgart" || team2 === "VfB Stuttgart") {
                    spiel_tor_liste = spiel['Goals']
                    console.log(spiel_tor_liste)
                    spiel_tor_liste = spiel['Goals']
                    console.log("Liste mit Toren aus dem Spiel" + spiel_tor_liste)
                }

                if (team1_tore > team2_tore) {
                    if (team1 === "VfB Stuttgart") {
                        console.log("VfB Tore bei Sieg:" + team1_tore)
                        zaehler_fuer_siege = zaehler_fuer_siege + team1_tore

                        zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + team1_tore
                        console.log("Tore Insgesamt:" + zaehler_fuer_tore_von_vfb)
                    }
                }

                if (team1_tore < team2_tore) {
                    if (team2 === "VfB Stuttgart") {
                        console.log("VfB Tore bei Sieg:" + team2_tore)
                        zaehler_fuer_siege = zaehler_fuer_siege + team2_tore

                        zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + team2_tore
                        console.log("Tore Insgesamt:" + zaehler_fuer_tore_von_vfb)
                    }
                }





                if (team1_tore === team2_tore) {
                    if (team2 === "VfB Stuttgart") {
                        console.log("VfB Tore bei Unentschieden:" + team2_tore)
                        zaehler_fuer_Unentschieden = zaehler_fuer_Unentschieden + team2_tore



                        zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + team2_tore
                        console.log("Tore Insgesamt:" + zaehler_fuer_tore_von_vfb)
                    }
                }
                if (team1_tore === team2_tore) {
                    if (team1 === "VfB Stuttgart") {
                        console.log("VfB Tore bei Unentschieden:" + team1_tore)
                        zaehler_fuer_Unentschieden = zaehler_fuer_Unentschieden + team1_tore
                        zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + team1_tore
                        console.log("Tore Insgesamt:" + zaehler_fuer_tore_von_vfb)
                    }
                }



                if (team1_tore < team2_tore) {
                    if (team1 === "VfB Stuttgart") {
                        console.log("VfB Tore bei Niederlage:" + team1_tore)
                        zaehler_fuer_niederlagen = zaehler_fuer_niederlagen + team1_tore

                        zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + team1_tore
                        console.log("Tore Insgesamt:" + zaehler_fuer_tore_von_vfb)
                    }
                }

                if (team1_tore > team2_tore) {
                    if (team2 === "VfB Stuttgart") {
                        console.log("VfB Tore bei Niederlage:" + team2_tore)
                        zaehler_fuer_niederlagen = zaehler_fuer_niederlagen + team2_tore

                        zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + team2_tore
                        console.log("Tore Insgesamt:" + zaehler_fuer_tore_von_vfb)
                    }
                }



                if (team1_tore > team2_tore) {
                    if (team1 === "VfB Stuttgart") {
                        console.log("VfB hat gewonnen")

                        zaehler_fuer_gewonnene_spiele = zaehler_fuer_gewonnene_spiele + 3
                        console.log("Gewonnene Spiele:" + zaehler_fuer_gewonnene_spiele)
                    }
                }

                if (team1_tore < team2_tore) {
                    if (team1 === "VfB Stuttgart") {
                        console.log("VfB hat gewonnen")
                        zaehler_fuer_gewonnene_spiele = zaehler_fuer_gewonnene_spiele + 3
                        console.log("Gewonnene Spiele:" + zaehler_fuer_gewonnene_spiele)
                    }
                }


                if (team1_tore === team2_tore) {
                    if (team1 === "VfB Stuttgart") {
                        console.log("VfB hat Unentschieden gespielt")
                        zaehler_fuer_Unentschiede_spiele = zaehler_fuer_Unentschiede_spiele + 1
                        console.log("Unentschiedene Spiele:" + zaehler_fuer_Unentschiede_spiele)
                    }
                }

                if (team1_tore === team2_tore) {
                    if (team2 === "VfB Stuttgart") {
                        console.log("VfB hat Unentschieden gespielt")
                        zaehler_fuer_Unentschiede_spiele = zaehler_fuer_Unentschiede_spiele + 1
                        console.log("Unentschiedene Spiele:" + zaehler_fuer_Unentschiede_spiele)
                    }
                }




                if (team1_tore < team2_tore) {
                    if (team1 === "VfB Stuttgart") {
                        console.log("VfB hat verloren")
                        zaehler_fuer_verlorene_spiele = zaehler_fuer_verlorene_spiele + 1
                        console.log("Verlorene Spiele:" + zaehler_fuer_verlorene_spiele)
                    }
                }

                if (team1_tore > team2_tore) {
                    if (team2 === "VfB Stuttgart") {
                        console.log("VfB hat verloren")
                        zaehler_fuer_verlorene_spiele = zaehler_fuer_verlorene_spiele + 1
                        console.log("Verlorene Spiele:" + zaehler_fuer_verlorene_spiele)
                    }
                }




                if (team1 === "VfB Stuttgart" || team2 === "VfB Stuttgart") {
                    zaehler_fuer_vfb_spiele = zaehler_fuer_vfb_spiele + 1
                }
                console.log("Gespielte Partien:" + zaehler_fuer_vfb_spiele)
                console.log()
            }
        }
    })



}








