import requests

def bestimme_endergebnis_aus_liste_mit_toren(aktuelle_liste_mit_allen_toren):
    for aktuelles_einzelnes_tor in aktuelle_liste_mit_allen_toren:
        Tore_team1 = aktuelles_einzelnes_tor['ScoreTeam1']
        Tore_team2 = aktuelles_einzelnes_tor['ScoreTeam2']
        ScoreTeam1 = (Tore_team1, Tore_team2)
    return ScoreTeam1

# ein einzelnes spiel muss ühergeben werden
def bestimme_namen_beider_teams(spiel):
    team_name1 = spiel['Team1']['TeamName']
    team_name2 = spiel['Team2']['TeamName']
    return team_name1, team_name2




alle_bundesliga_ergebnisse = requests.get('https://www.openligadb.de/api/getmatchdata/bl2/2019')
alle_bundesliga_ergebnisse = alle_bundesliga_ergebnisse.json() # Erzeugen einer Liste aus dem Antwort-Objekt
# print(r)    # Gesamte Liste
# print(r[0]) # Erstes Element einer Liste
einzelnes_spiel = alle_bundesliga_ergebnisse[0]
aktuelle_matchid = einzelnes_spiel['MatchID']
# print(aktuelle_matchid)
# print(r[0]['Team1']['TeamName'])

aktuelle_spielergebnisse = einzelnes_spiel['MatchResults'] # liste mit spielergebnissen
print(aktuelle_spielergebnisse)
endergebnis = aktuelle_spielergebnisse[0]

# print("Ausgabe der Namen der Teams:")
team1, team2 = bestimme_namen_beider_teams(einzelnes_spiel)
# print(team1)
#print(team2)
# team2 = einzelnes_spiel ['Team2']



ergebnisbeschreibung = endergebnis['ResultDescription']
# print(ergebnisbeschreibung)

punkte_team1 = endergebnis['PointsTeam1']
punkte_team2 = endergebnis['PointsTeam2']

# print("Team1: " + str(punkte_team1))
# print("Team2: " + str(punkte_team2))

aktuelles_Torverhältnis = einzelnes_spiel['Goals'] #Liste mit Torverhältnis
# print(aktuelles_Torverhältnis )
Torverhältnis = aktuelles_Torverhältnis
alle_aktuellen_tore_als_liste = aktuelles_Torverhältnis

tor1 = Torverhältnis[0]
Tore_team1 = tor1['ScoreTeam1']
Tore_team2 = Torverhältnis[0]['ScoreTeam2']
# print("Länge der Liste: " + str(len(Torverhältnis)))
# print("Team1: " + str(Tore_team1))
# print("Team2: " + str(Tore_team2))
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


# verein = " SV Darmstadt 98"

        # for spiel in alle_bundesliga_ergebnisse:
#     # print("Aktuelles Spiel" + str(spiel))
#     # variable "spiel" enthält das aktuelle spiel bspw:
#     '''
#     {
#         "MatchID": 55583,
#         "MatchDateTime": "2019-07-26T20:30:00",
#         "TimeZoneID": "W. Europe Standard Time",
#         "LeagueId": 4363,
#         "LeagueName": "2. Fußball-Bundesliga 2019/2020",
#         "MatchDateTimeUTC": "2019-07-26T18:30:00Z",
#         "Group": {
#             "GroupName": "1. Spieltag",
#             "GroupOrderID": 1,
#             "GroupID": 34234
#         },
#         "Team1": {
#             "TeamId": 16,
#             "TeamName": "VfB Stuttgart",
#             "ShortName": "Stuttgart",
#             "TeamIconUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/VfB_Stuttgart_1893_Logo.svg/921px-VfB_Stuttgart_1893_Logo.svg.png",
#             "TeamGroupName": null
#         },
#         "Team2": {
#             "TeamId": 55,
#             "TeamName": "Hannover 96",
#             "ShortName": "Hannover",
#             "TeamIconUrl": "https://upload.wikimedia.org/wikipedia/commons/c/cd/Hannover_96_Logo.svg",
#             "TeamGroupName": null
#         },
#         "LastUpdateDateTime": "2019-07-26T22:34:31.777",
#         "MatchIsFinished": true,
#         "MatchResults": [
#             {
#                 "ResultID": 87970,
#                 "ResultName": "Endergebnis",
#                 "PointsTeam1": 2,
#                 "PointsTeam2": 1,
#                 "ResultOrderID": 2,
#                 "ResultTypeID": 2,
#                 "ResultDescription": "Ergebnis nach Ende der offiziellen Spielzeit"
#             },
#             {
#                 "ResultID": 87971,
#                 "ResultName": "Halbzeit",
#                 "PointsTeam1": 2,
#                 "PointsTeam2": 1,
#                 "ResultOrderID": 1,
#                 "ResultTypeID": 1,
#                 "ResultDescription": "Zwischenstand zur Halbzeit"
#             }
#         ],
#         "Goals": [
#             {
#                 "GoalID": 78635,
#                 "ScoreTeam1": 1,
#                 "ScoreTeam2": 0,
#                 "MatchMinute": 29,
#                 "GoalGetterID": 1848,
#                 "GoalGetterName": "Mario Gomez",
#                 "IsPenalty": false,
#                 "IsOwnGoal": false,
#                 "IsOvertime": false,
#                 "Comment": null
#             },
#             {
#                 "GoalID": 78636,
#                 "ScoreTeam1": 2,
#                 "ScoreTeam2": 0,
#                 "MatchMinute": 36,
#                 "GoalGetterID": 16031,
#                 "GoalGetterName": "Daniel Didavi",
#                 "IsPenalty": false,
#                 "IsOwnGoal": false,
#                 "IsOvertime": false,
#                 "Comment": null
#             },
#             {
#                 "GoalID": 78638,
#                 "ScoreTeam1": 2,
#                 "ScoreTeam2": 1,
#                 "MatchMinute": 39,
#                 "GoalGetterID": 17644,
#                 "GoalGetterName": "Maxime Awoudja",
#                 "IsPenalty": false,
#                 "IsOwnGoal": true,
#                 "IsOvertime": false,
#                 "Comment": null
#             }
#         ],
#         "Location": null,
#         "NumberOfViewers": null
#     },
#     '''
#
#     team1_tore = 0
#     team2_tore = 0
#
#     team1, team2 = bestimme_namen_beider_teams(spiel)
#     if team1 == "Hamburger SV" or team2 == "Hamburger SV":
#         print(team1 + " Spielt gegen " + team2)
#         # hiet wissen wir, dass es ein spiel vom VfB Stuttgart ist
#
#         spiel_tor_liste = spiel['Goals']
#         '''
#         Beispielinhalt von Variable "aktuelles_Torverhältnis"
#         Ist eine Liste die 3 Einträge enthält
#         [{
#                 "GoalID": 78635,
#                 "ScoreTeam1": 1,
#                 "ScoreTeam2": 0,
#                 "MatchMinute": 29,
#                 "GoalGetterID": 1848,
#                 "GoalGetterName": "Mario Gomez",
#                 "IsPenalty": false,
#                 "IsOwnGoal": false,
#                 "IsOvertime": false,
#                 "Comment": null
#             },
#             {
#                 "GoalID": 78636,
#                 "ScoreTeam1": 2,
#                 "ScoreTeam2": 0,
#                 "MatchMinute": 36,
#                 "GoalGetterID": 16031,
#                 "GoalGetterName": "Daniel Didavi",
#                 "IsPenalty": false,
#                 "IsOwnGoal": false,
#                 "IsOvertime": false,
#                 "Comment": null
#             },
#             {
#                 "GoalID": 78638,
#                 "ScoreTeam1": 2,
#                 "ScoreTeam2": 1,
#                 "MatchMinute": 39,
#                 "GoalGetterID": 17644,
#                 "GoalGetterName": "Maxime Awoudja",
#                 "IsPenalty": false,
#                 "IsOwnGoal": true,
#                 "IsOvertime": false,
#                 "Comment": null
#             }]
#
#             tor = spiel_tor_liste[0]
#             tor = spiel_tor_liste[1]
#             tor = spiel_tor_liste[2]
#
#             for tor in spiel_tor_liste: 3mal ausgeführt
#                 print(tor['GoalID'])
#
#         '''
#         zeitpunkt_des_spiels = spiel['MatchDateTime']  # zugriff auf Zeipunkt des Spiels
#         aktuelles_Datum = "2020-01-23T08:30:00"
#         # Prüfung, ob Zeitpunkt des Spiels in der Zukunft oder Vergangenheit liegt
#         if aktuelles_Datum < zeitpunkt_des_spiels:
#             print("Das Spiel wurde noch nicht gespielt.")
#         else:  # alles was in der Vergangeheit passiert ist
#             print("Das Spiel hat am " + str(zeitpunkt_des_spiels) + " stattgefunden.")
#             if len(
#                     spiel_tor_liste) == 0:  # Prüfung auf länge der Liste -> leere liste (länge 0) heißt das spiel ist unentschieden ausgegangen
#                 print("Spiel ist 0:0 ausgegangen.")
#             else:
#                 erstes_geschossenes_tor = spiel_tor_liste[0]  # zugriff auf erstes Tor aus der Tor Liste
#                 print(erstes_geschossenes_tor)
#
#             # print('Tor ID: ' + str(tor['GoalID']))
#             # Endergebnis_des_spiels = spiel('Goals')
#             # if :
#             #   print("Das Spiel ist" +str(Endergebnis_des_spiels) + "ausgegangen.")
#
#             team1, team2 = bestimme_namen_beider_teams(spiel)
#             for tor in spiel_tor_liste:
#                 print("Ein Tor ist gefallen")
#                 team1_tore = tor['ScoreTeam1']
#                 team2_tore = tor['ScoreTeam2']
#                 print('H: ' + str(team1_tore))
#                 print('A: ' + str(team2_tore))
#
#             liste_mit_spielergebnissen = spiel['MatchResults']
#             print(liste_mit_spielergebnissen)
#             endspielergebnis = liste_mit_spielergebnissen[0]
#             print(endspielergebnis)
#             PointsTeam1 = endspielergebnis['PointsTeam1']
#             PointsTeam2 = endspielergebnis['PointsTeam2']
#             if team1 == "Hamburger SV" or team2 == "Hamburger SV":
#                 print("Heim:" + str(PointsTeam1) + " Auswerts:" + str(PointsTeam2))
#
#                 spiel_tor_liste = spiel['Goals']
#                 print(spiel_tor_liste)
#
#                 spiel_tor_liste = spiel['Goals']
#                 print("Liste mit Toren aus dem Spiel" + str(spiel_tor_liste))
#
#                 if team1_tore > team2_tore:
#                     if team1 == "Hamburger SV":
#                         print("HSV Tore bei Sieg:" + str(team1_tore))
#                         zaehler_fuer_siege = zaehler_fuer_siege + team1_tore
#                         # print("Gewonnene Spiele": + str(zaehler_fuer_siege))
#                         zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + team1_tore
#                         print("Tore Insgesamt:" + str(zaehler_fuer_tore_von_vfb))
#                         print()
#
#                 if team1_tore < team2_tore:
#                     if team2 == "Hamburger SV":
#                         print("HSV Tore bei Sieg:" + str(team2_tore))
#                         zaehler_fuer_siege = zaehler_fuer_siege + team2_tore
#                         # print("Gewonnene Spiele": + str(zaehler_fuer_siege))
#                         zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + team2_tore
#                         print("Tore Insgesamt:" + str(zaehler_fuer_tore_von_vfb))
#
#                 if team1_tore == team2_tore:
#                     if team2 == "Hamburger SV":
#                         print("HSV Tore bei Unentschieden:" + str(team1_tore))
#                         zaehler_fuer_Unentschieden = zaehler_fuer_Unentschieden + team1_tore
#                         # print("Unentschiedene Spiele:" + str(zaehler_fuer_Unentschieden))
#                         zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + team1_tore
#                         print("Tore Insgesamt:" + str(zaehler_fuer_tore_von_vfb))
#
#                         # if len(spiel_tor_liste) == 0:
#                         #     zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + 0
#                         #     print(zaehler_fuer_tore_von_vfb + 0)
#                         #     print("Keine Tore gefallen")
#
#                 if team1_tore == team2_tore:
#                     if team1 == "Hamburger SV":
#                         print("HSV Tore bei Unentschieden:" + str(team2_tore))
#                         zaehler_fuer_Unentschieden = zaehler_fuer_Unentschieden + team2_tore
#                         # print("Unentschiedene Spiele:" + str(zaehler_fuer_Unentschieden))
#                         zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + team2_tore
#                         print("Tore Insgesamt:" + str(zaehler_fuer_tore_von_vfb))
#
#                         # if len(spiel_tor_liste) == 0:
#                         #     zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + 0
#                         #     print(zaehler_fuer_tore_von_vfb + 0)
#                         #     print("Keine Tore gefallen")
#
#                 if team1_tore < team2_tore:
#                     if team1 == "Hamburger SV":
#                         print("HSV Tore bei Niederlage:" + str(team1_tore))
#                         zaehler_fuer_niederlagen = zaehler_fuer_niederlagen + team1_tore
#
#                         zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + team1_tore
#                         print("Tore Insgesamt:" + str(zaehler_fuer_tore_von_vfb))
#
#                 if team1_tore > team2_tore:
#                     if team2 == "Hamburger SV":
#                         print("HSV Tore bei Niederlage:" + str(team2_tore))
#                         zaehler_fuer_niederlagen = zaehler_fuer_niederlagen + team2_tore
#                         # print("Verlorene Spiele:" + str(zaehler_fuer_niederlagen))
#                         zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + team2_tore
#                         print("Tore Insgesamt:" + str(zaehler_fuer_tore_von_vfb))
#                 # print("Team 1 Tore" + str(team1_tore))
#                 # print("Team 2 Tore" + str(team2_tore))
#
#                 if team1_tore > team2_tore:
#                     if team1 == "Hamburger SV":
#                         print("HSV hat gewonnen")
#                         zaehler_fuer_gewonnene_spiele = zaehler_fuer_gewonnene_spiele + 3
#                         print("Gewonnene Spiele:" + str(zaehler_fuer_gewonnene_spiele))
#
#                 if team1_tore < team2_tore:
#                     if team2 == "Hamburger SV":
#                         print("HSV hat gewonnen")
#                         zaehler_fuer_gewonnene_spiele = zaehler_fuer_gewonnene_spiele + 3
#                         print("Gewonnene Spiele:" + str(zaehler_fuer_gewonnene_spiele))
#
#                 if team1_tore == team2_tore:
#                     if team1 == "Hamburger SV":
#                         print("HSV hat Unentschieden gespielt")
#                         zaehler_fuer_Unentschiede_spiele = zaehler_fuer_Unentschiede_spiele + 1
#                         print("Unentschiedene Spiele:" + str(zaehler_fuer_Unentschiede_spiele))
#
#                 if team1_tore == team2_tore:
#                     if team2 == "Hamburger SV":
#                         print("HSV hat Unentschieden gespielt")
#                         zaehler_fuer_Unentschiede_spiele = zaehler_fuer_Unentschiede_spiele + 1
#                         print("Unentschiedene Spiele:" + str(zaehler_fuer_Unentschiede_spiele))
#
#                 if team1_tore < team2_tore:
#                     if team1 == "Hamburger SV":
#                         print("HSV hat verloren")
#                         zaehler_fuer_verlorene_spiele = zaehler_fuer_verlorene_spiele + 1
#                         print("Verlorene Spiele:" + str(zaehler_fuer_verlorene_spiele))
#
#                 if team1_tore > team2_tore:
#                     if team2 == "Hamburger SV":
#                         print("HSV hat verloren")
#                         zaehler_fuer_verlorene_spiele = zaehler_fuer_verlorene_spiele + 1
#                         print("Verlorene Spiele:" + str(zaehler_fuer_verlorene_spiele))
#                 # print("tor;    "+ str(team1_tore) + "         " + str(team2_tore))
#
#                 if team1 == "Hamburger SV" or team2 == "Hamburger SV":
#                     zaehler_fuer_vfb_spiele = zaehler_fuer_vfb_spiele + 1
#                     print("Gespielte Partien:" + str(zaehler_fuer_vfb_spiele))

        #print('\n')


tor = {}

for spiel in alle_bundesliga_ergebnisse:
    team1_tore = 0
    team2_tore = 0

    team1, team2 = bestimme_namen_beider_teams(spiel)
    if team1 == "VfB Stuttgart" or team2 == "VfB stuttgart":
        print(team1 + " Spielt gegen " + team2)
        # hiet wissen wir, dass es ein spiel vom VfB Stuttgart ist

        spiel_tor_liste = spiel['Goals']
        
        zeitpunkt_des_spiels = spiel['MatchDateTime']   #zugriff auf Zeipunkt des Spiels
        aktuelles_Datum = "2020-01-23T08:30:00"
        # Prüfung, ob Zeitpunkt des Spiels in der Zukunft oder Vergangenheit liegt
        if aktuelles_Datum < zeitpunkt_des_spiels:
            print("Das Spiel wurde noch nicht gespielt.")
        else: # alles was in der Vergangeheit passiert ist
            print("Das Spiel hat am " + str(zeitpunkt_des_spiels) + " stattgefunden.")
            if len(spiel_tor_liste) == 0: # Prüfung auf länge der Liste -> leere liste (länge 0) heißt das spiel ist unentschieden ausgegangen
                print("Spiel ist 0:0 ausgegangen.")
            else:
                erstes_geschossenes_tor = spiel_tor_liste[0]        # zugriff auf erstes Tor aus der Tor Liste
                print(erstes_geschossenes_tor)

            #print('Tor ID: ' + str(tor['GoalID']))
        # Endergebnis_des_spiels = spiel('Goals')
        # if :
        #   print("Das Spiel ist" +str(Endergebnis_des_spiels) + "ausgegangen.")

            team1, team2 = bestimme_namen_beider_teams(spiel)
            for tor in spiel_tor_liste:
                print("Ein Tor ist gefallen")
                team1_tore = tor['ScoreTeam1']
                team2_tore = tor['ScoreTeam2']
                print('H: ' + str(team1_tore))
                print('A: ' + str(team2_tore))

            liste_mit_spielergebnissen = spiel['MatchResults']
            print(liste_mit_spielergebnissen)
            endspielergebnis = liste_mit_spielergebnissen[0]
            print(endspielergebnis)
            PointsTeam1 = endspielergebnis['PointsTeam1']
            PointsTeam2 = endspielergebnis['PointsTeam2']
            if team1 == "VfB Stuttgart" or team2 == "VfB Stuttgart":
                print("Heim:"  + str(PointsTeam1) + " Auswerts:" + str(PointsTeam2))

                spiel_tor_liste = spiel['Goals']
                print(spiel_tor_liste)

                spiel_tor_liste = spiel['Goals']
                print("Liste mit Toren aus dem Spiel"+ str(spiel_tor_liste))


                if team1_tore > team2_tore:
                    if team1 == "VfB Stuttgart":
                        print("VfB Tore bei Sieg:" + str(team1_tore))
                        zaehler_fuer_siege = zaehler_fuer_siege + team1_tore
                        # print("Gewonnene Spiele": + str(zaehler_fuer_siege))
                        zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + team1_tore
                        print("Tore Insgesamt:" + str(zaehler_fuer_tore_von_vfb))
                        print()

                if team1_tore < team2_tore:
                    if team2 == "VfB Stuttgart":
                        print("VfB Tore bei Sieg:" + str(team2_tore))
                        zaehler_fuer_siege = zaehler_fuer_siege + team2_tore
                        # print("Gewonnene Spiele": + str(zaehler_fuer_siege))
                        zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + team2_tore
                        print("Tore Insgesamt:" + str(zaehler_fuer_tore_von_vfb))


                if team1_tore == team2_tore:
                    if team2 == "VfB Stuttgart":
                        print("VfB Tore bei Unentschieden:" + str(team1_tore))
                        zaehler_fuer_Unentschieden = zaehler_fuer_Unentschieden + team1_tore
                        # print("Unentschiedene Spiele:" + str(zaehler_fuer_Unentschieden))
                        zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + team1_tore
                        print("Tore Insgesamt:" + str(zaehler_fuer_tore_von_vfb))

                        # if len(spiel_tor_liste) == 0:
                        #     zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + 0
                        #     print(zaehler_fuer_tore_von_vfb + 0)
                        #     print("Keine Tore gefallen")


                if team1_tore == team2_tore:
                    if team1 == "VfB Stuttgart":
                        print("VfB Tore bei Unentschieden:" + str(team2_tore))
                        zaehler_fuer_Unentschieden = zaehler_fuer_Unentschieden + team2_tore
                        # print("Unentschiedene Spiele:" + str(zaehler_fuer_Unentschieden))
                        zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + team2_tore
                        print("Tore Insgesamt:" + str(zaehler_fuer_tore_von_vfb))

                        # if len(spiel_tor_liste) == 0:
                        #     zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + 0
                        #     print(zaehler_fuer_tore_von_vfb + 0)
                        #     print("Keine Tore gefallen")


                if team1_tore < team2_tore:
                    if team1 == "VfB Stuttgart":
                        print("VfB Tore bei Niederlage:" + str(team1_tore))
                        zaehler_fuer_niederlagen = zaehler_fuer_niederlagen + team1_tore

                        zaehler_fuer_tore_von_vfb = zaehler_fuer_tore_von_vfb + team1_tore
                        print("Tore Insgesamt:" + str(zaehler_fuer_tore_von_vfb))


                if team1_tore > team2_tore:
                    if team2 == "VfB Stuttgart":
                        print("VfB Tore bei Niederlage:" + str(team2_tore))
                        zaehler_fuer_niederlagen = zaehler_fuer_niederlagen + team2_tore
                        # print("Verlorene Spiele:" + str(zaehler_fuer_niederlagen))
                        zaehler_fuer_tore_von_vfb =zaehler_fuer_tore_von_vfb + team2_tore
                        print("Tore Insgesamt:" + str(zaehler_fuer_tore_von_vfb))
                # print("Team 1 Tore" + str(team1_tore))
                # print("Team 2 Tore" + str(team2_tore))


                if team1_tore > team2_tore:
                    if team1 == "VfB Stuttgart":
                        print("VfB hat gewonnen")
                        zaehler_fuer_gewonnene_spiele = zaehler_fuer_gewonnene_spiele + 3
                        print("Gewonnene Spiele:" + str(zaehler_fuer_gewonnene_spiele))

                if team1_tore < team2_tore:
                    if team2 == "VfB Stuttgart":
                        print("VfB hat gewonnen")
                        zaehler_fuer_gewonnene_spiele = zaehler_fuer_gewonnene_spiele + 3
                        print("Gewonnene Spiele:" + str(zaehler_fuer_gewonnene_spiele))

                if team1_tore == team2_tore:
                    if team1 == "VfB Stuttgart":
                        print("VfB hat Unentschieden gespielt")
                        zaehler_fuer_Unentschiede_spiele = zaehler_fuer_Unentschiede_spiele + 1
                        print("Unentschiedene Spiele:" + str(zaehler_fuer_Unentschiede_spiele))

                if team1_tore == team2_tore:
                    if team2 == "VfB Stuttgart":
                        print("VfB hat Unentschieden gespielt")
                        zaehler_fuer_Unentschiede_spiele = zaehler_fuer_Unentschiede_spiele + 1
                        print("Unentschiedene Spiele:" + str(zaehler_fuer_Unentschiede_spiele))

                if team1_tore < team2_tore:
                    if team1 == "VfB Stuttgart":
                        print("VfB hat verloren")
                        zaehler_fuer_verlorene_spiele = zaehler_fuer_verlorene_spiele + 1
                        print("Verlorene Spiele:" + str(zaehler_fuer_verlorene_spiele))

                if team1_tore > team2_tore:
                    if team2 == "VfB Stuttgart":
                        print("VfB hat verloren")
                        zaehler_fuer_verlorene_spiele = zaehler_fuer_verlorene_spiele + 1
                        print("Verlorene Spiele:" + str(zaehler_fuer_verlorene_spiele))
                #print("tor;    "+ str(team1_tore) + "         " + str(team2_tore))

                if team1 == "VfB Stuttgart" or team2 == "VfB Stuttgart":
                     zaehler_fuer_vfb_spiele = zaehler_fuer_vfb_spiele + 1
                     print("Gespielte Partien:" + str(zaehler_fuer_vfb_spiele))


        print('\n')



print('\n')
print("Tore bei Siegen:\t\t\t\t" + str(zaehler_fuer_siege))
print("Tore bei Unentschieden:\t\t\t" + str (zaehler_fuer_Unentschieden))
print("Tore bei niederlagen\t\t\t" + str (zaehler_fuer_niederlagen))
print("Gesamtanzahl Tore:\t\t\t\t"+ str(zaehler_fuer_tore_von_vfb))
print('\n')
print("Gespielte Partien:\t\t\t\t" + str(zaehler_fuer_vfb_spiele))
print('\n')
print("Punkte bei Siegen:\t\t\t\t" + str(zaehler_fuer_gewonnene_spiele))
print("Punkte bei Unentschieden:\t\t" + str(zaehler_fuer_Unentschiede_spiele))
print("Verlorene Spiele:\t\t\t\t" + str(zaehler_fuer_verlorene_spiele))
ergebnis = zaehler_fuer_gewonnene_spiele + zaehler_fuer_Unentschiede_spiele
print("Gesamtanzahl Punkte:\t\t\t" + str(ergebnis))


                # team1, team2 = bestimme_namen_beider_teams(spiel)
                # for tor in spiel_tor_liste:
                #     spiel_tor_liste = spiel['Goals']
                #
                # team1_tore = tor['ScoreTeam1']
                # team2_tore = tor['ScoreTeam2']
                #
                # if team1 == "VfB Stuttgart" or team2 == "VfB Stuttgart":
                #     print("Alle VfB Tore": + str(team1_tore) + str(team2_tore))
        #print('\n')