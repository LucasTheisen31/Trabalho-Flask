# Controller com funções de rota
# Importações necessárias
from flask import render_template, redirect, request, flash, url_for
from app import app, db, login_manager
from app.models.tables import User, Task
from app.models.forms import LoginForm,  RegisterForm, TaskForm
from flask_login import login_user, login_required, logout_user, current_user

# Carrega os dados do usuário armazenados na sessão quando logado
@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

# Rota da página inicial
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if not current_user.is_authenticated: # Se o usuário não estiver logado, redireciono o mesmo para a tela de login
        return redirect(url_for('login'))
    user_tasks = Task.query.filter_by(user_id=current_user.id).all()
    form = TaskForm()  # Crie uma instância do formulário TaskForm
    if request.method == 'POST' and form.validate_on_submit():
        try:
            description = form.task_description.data
            new_task = Task(description=description, user_id=current_user.id)
            db.session.add(new_task)
            db.session.commit()
            flash('Tarefa adicionada com sucesso!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            print(f"Erro ao adicionar a tarefa: {e}")
            flash('Erro ao adicionar a tarefa. Tente novamente.', 'danger')
            
    return render_template('index.html', tasks=user_tasks, form=form)

# Rota de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        user = User.query.filter_by(name=name).first() # Verifica se o usuário existe

        if user and user.password == password: # Se o usuário existe e a senha esta correta
            login_user(user) # Faz o login do usuário
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Credenciais inválidas. Tente novamente.', 'danger')

    return render_template('login.html', form=form)

# Rota de registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data

        existing_user = User.query.filter_by(name=name).first()

        if existing_user:
            flash('Usuário já existe. Escolha outro nome de usuário.', 'danger')
        else:
            new_user = User(name=name, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('Cadastro realizado com sucesso!', 'success')
            return redirect(url_for('login'))

    return render_template('register.html', form=form)

# Rota de logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('login'))


@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    # Obtenha a tarefa com base no task_id
    task = Task.query.get_or_404(task_id)

    # Crie um formulário de edição de tarefa
    form = TaskForm()

    if request.method == 'POST' and form.validate_on_submit():
        # Atualize os detalhes da tarefa com os dados do formulário
        task.description = form.task_description.data
        db.session.commit()
        flash('Tarefa editada com sucesso!', 'success')
        return redirect(url_for('index'))

    # Preencha o formulário com os detalhes da tarefa atual
    form.task_description.data = task.description

    return render_template('edit_task.html', form=form, task=task)

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    
    return redirect(url_for('index'))


# @app.route('/add_task', methods=['POST'])
# @login_required
# def add_task():
#     form = TaskForm()
#     if form.validate_on_submit():
#         try:
#             description = form.task_description.data
#             new_task = Task(description=description, user_id=current_user.id)
#             db.session.add(new_task)
#             db.session.commit()
#             flash('Tarefa adicionada com sucesso!', 'success')
#         except Exception as e:
#             print(f"Erro ao adicionar a tarefa: {e}")
#             flash('Erro ao adicionar a tarefa. Tente novamente.', 'danger')
    
#     return redirect(url_for('index'))