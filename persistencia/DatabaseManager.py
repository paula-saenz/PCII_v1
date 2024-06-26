import mysql.connector as mysql

class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def insert_jugador(self, jugador_data):
        try:
            connection = mysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            cursor = connection.cursor()

            insert_query = """
                INSERT INTO jugadores
                (name, barter, bid, floor, height, id_mister, id_competition_mister, id_team_mister, id_marca, multiplier,
                nationality, offer, owner, photoUrl, position, status, video_frame, weight, id_as, birthday, id_biwenger,
                created, id_gsm, id_opta, id_rf, id_sofascore, updated, attacking, creativity, defending, tactical, technical,
                aerial, anticipation, ball_distribution, saves, tactical_gk, jersey_number, preferred_foot, contract_until,
                proposed_market_value, debut_seleccion, id_seleccion, retired)
                VALUES
                (%(name)s, %(barter)s, %(bid)s, %(floor)s, %(height)s, %(id_mister)s, %(id_competition_mister)s, %(id_team_mister)s,
                %(id_marca)s, %(multiplier)s, %(nationality)s, %(offer)s, %(owner)s, %(photoUrl)s, %(position)s, %(status)s,
                %(video_frame)s, %(weight)s, %(id_as)s, %(birthday)s, %(id_biwenger)s, %(created)s, %(id_gsm)s, %(id_opta)s,
                %(id_rf)s, %(id_sofascore)s, %(updated)s, %(attacking)s, %(creativity)s, %(defending)s, %(tactical)s, %(technical)s,
                %(aerial)s, %(anticipation)s, %(ballDistribution)s, %(saves)s, %(tacticalGK)s, %(jerseyNumber)s, %(preferredFoot)s,
                %(contractUntil)s, %(proposedMarketValue)s, %(debutTimestampSeleccion)s, %(idSeleccion)s, %(retired)s)
            """

            cursor.execute(insert_query, jugador_data)
            connection.commit()
        except Exception as e:
            print(f"Error al insertar en la base de datos: {e}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()
            
        
    def insert_equipo(self, equipo_data):
        try:
            connection = mysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            cursor = connection.cursor()

            insert_query = """
                INSERT INTO Equipos
                (id, id_as, id_biwenger, id_competition, teamLogoUrl, name, updated)
                VALUES
                (%(id)s, %(id_as)s, %(id_biwenger)s, %(id_competition)s, %(teamLogoUrl)s, %(name)s, %(updated)s)
            """

            cursor.execute(insert_query, equipo_data)
            connection.commit()
        except Exception as e:
            print(f"Error al insertar en la base de datos: {e}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()
            

