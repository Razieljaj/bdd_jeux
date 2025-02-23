import sqlite3

def recuperer_jeux_par_nom(nom):
    """Renvoie les informations des jeux qui ont un nom ressemblant à la recherche nom passée en paramètre"""
    conn = sqlite3.connect('Steam_Like.db')
    cur = conn.cursor()
    res = cur.execute("""SELECT * FROM Jeux WHERE nom LIKE ?""",('%' + nom + '%',))
    jeux = res.fetchall()
    conn.close()
    return jeux

def chaque_jeu(tri):
    """ permet renvoie les informations relatives aux jeux triés comme l'utilisateur l'a choisi (avec le paramètre tri)"""
    conn = sqlite3.connect('Steam_Like.db')
    cur = conn.cursor()
    if tri == "tri_nom":
        res = cur.execute("""SELECT * FROM Jeux
INNER JOIN Statut
ON Jeux.id_statut = Statut.id
INNER JOIN Type
ON Jeux.id_type = Type.id ORDER BY Jeux.nom;""")
    elif tri == "tri_date":
        res = cur.execute("""SELECT * FROM Jeux
INNER JOIN Statut
ON Jeux.id_statut = Statut.id
INNER JOIN Type
ON Jeux.id_type = Type.id ORDER BY Jeux.date;""")
    elif tri == "tri_type":
        res = cur.execute("""SELECT * FROM Jeux
INNER JOIN Statut
ON Jeux.id_statut = Statut.id
INNER JOIN Type
ON Jeux.id_type = Type.id ORDER BY Type.nom;""")
    elif tri == "tri_statut":
        res = cur.execute("""SELECT * FROM Jeux
INNER JOIN Statut
ON Jeux.id_statut = Statut.id
INNER JOIN Type
ON Jeux.id_type = Type.id ORDER BY Statut.nom;""")
    else:
        res = cur.execute("""SELECT * FROM Jeux
INNER JOIN Statut
ON Jeux.id_statut = Statut.id
INNER JOIN Type
ON Jeux.id_type = Type.id;""")

    jeux = res.fetchall()
    conn.close()
    return jeux

def info_jeu(id):
    """ renvoie toutes les infomations liées a un jeux en comprennant toute les tables donc : la table jeux , la table developpeur , la table statut et la table type"""
    conn = sqlite3.connect('Steam_Like.db')
    cur = conn.cursor()
    res = cur.execute("""SELECT * FROM Jeux
INNER JOIN Statut
ON Jeux.id_statut = Statut.id
INNER JOIN Type
ON Jeux.id_type = Type.id
INNER JOIN Developpeur
ON Jeux.id_developpeur = Developpeur.id
WHERE Jeux.id = ?;""",(id,))
    jeux = res.fetchall()
    conn.close()
    return jeux

def ajouter(titre,prix,date,id_statut,id_type,id_developpeur):
    """Toutes les informations d'un jeu sont demandées en paramètre pour qu'il soit ajouté dans la base de données"""
    conn = sqlite3.connect('Steam_Like.db')
    cur = conn.cursor()
    res = cur.execute("""INSERT INTO Jeux VALUES(null,?,?,?,?,?,?,'default.jpg');""",(titre,prix,date,id_statut,id_type,id_developpeur)) # Une image par défaut est ajouté au jeu car l'utilisateur ne peut pas la fournir
    conn.commit()
    conn.close()
    return ('Fini!')

def supprimer(id_jeu):
    """Supprime le jeu dont l'id est passée en paramètre"""
    conn = sqlite3.connect('Steam_Like.db')
    cur = conn.cursor()
    res = cur.execute("""DELETE FROM Jeux WHERE id = ?;""",(id_jeu,))
    conn.commit()
    conn.close()

