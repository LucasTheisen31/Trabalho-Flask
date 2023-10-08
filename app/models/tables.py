from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique = True)
    password = db.Column(db.String, nullable=False)

    # ---------------
    # Propriedades e métodos para utilizar LoginManager:
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)
    # ---------------
    
    #construtor
    def __init__(self, name, password):
        self.name = name
        self.password = password


    #toString
    def __repr__(self):
        return f"<User(id={self.id}, name={self.name})>"
    

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) #id do usuario 

    user = db.relationship('User', foreign_keys=user_id) #relacionamento
    
    #construtor
    def __init__(self, description, user_id):
        self.description = description
        self.user_id = user_id

    #toString
    def __repr__(self):
        return f"<Task(id={self.id}, description={self.description}, user={self.user.name})>"