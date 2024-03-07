import mysql.connector


class Jugador:
    def __init__(self, name, barter, bid, floor, height, id_mister, id_competition_mister, id_team_mister, id_marca,
                 multiplier, nationality, offer, owner, photoUrl, position, status, video_frame, weight, id_as,
                 birthday, id_biwenger, created, id_gsm, id_opta, id_rf, id_sofascore, updated, attacking, creativity,
                 defending, tactical, technical, aerial, anticipation, ballDistribution, saves, tacticalGK, jerseyNumber,
                 preferredFoot, contractUntil, proposedMarketValue, debutTimestampSeleccion, idSeleccion, retired):
        self.name = name
        self.barter = barter
        self.bid = bid
        self.floor = floor
        self.height = height
        self.id_mister = id_mister
        self.id_competition_mister = id_competition_mister
        self.id_team_mister = id_team_mister
        self.id_marca = id_marca
        self.multiplier = multiplier
        self.nationality = nationality
        self.offer = offer
        self.owner = owner
        self.photoUrl = photoUrl
        self.position = position
        self.status = status
        self.video_frame = video_frame
        self.weight = weight
        self.id_as = id_as
        self.birthday = birthday
        self.id_biwenger = id_biwenger
        self.created = created
        self.id_gsm = id_gsm
        self.id_opta = id_opta
        self.id_rf = id_rf
        self.id_sofascore = id_sofascore
        self.updated = updated
        self.attacking = attacking
        self.creativity = creativity
        self.defending = defending
        self.tactical = tactical
        self.technical = technical
        self.aerial = aerial
        self.anticipation = anticipation
        self.ballDistribution = ballDistribution
        self.saves = saves
        self.tacticalGK = tacticalGK
        self.jerseyNumber = jerseyNumber
        self.preferredFoot = preferredFoot
        self.contractUntil = contractUntil
        self.proposedMarketValue = proposedMarketValue
        self.debutTimestampSeleccion = debutTimestampSeleccion
        self.idSeleccion = idSeleccion
        self.retired = retired

    def insert_into_database(self):
        # Establish a connection to your MySQL database
        connection = mysql.connector.connect(
            host='93.93.118.169',
            user='baboo',
            password='baboo2024',
            database='baboo_manager'
        )

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Insert data into the jugadores table
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

        # Convert Jugador object attributes to a dictionary
        player_data = self.__dict__

        cursor.execute(insert_query, player_data)

        # Commit the changes
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()
