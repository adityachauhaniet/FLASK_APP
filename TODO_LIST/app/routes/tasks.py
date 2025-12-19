from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db #importing the database instance
from app.models import Task, User #importing the Task model for so that we can interact with the tasks table in the database

#ek blueprint object create karte hain for task routes so that we can organize our routes related to tasks
tasks_bp = Blueprint('tasks', __name__) #name of the blueprint(tasks) and module name(__name__)



# ------------------------------------------------ Helper: check login -----------------------------

def get_current_user_id():
    user_id = session.get('user_id')
    if not user_id:
        flash('Please login first', 'warning')
        return None
    return user_id



#----------------------------------------route to display all tasks of logged-in user ---------------------------

@tasks_bp.route('/') #home route to display all tasks
def view_tasks():
    #pahle check karte hain ki user logged in hai ya nahi
    user_id = get_current_user_id() #ye function user id return karta h
    if 'user_id' not in session: #if user_id is None
        # flash('Please login to view your tasks', 'warning')#flash message with category warning
        return redirect(url_for('auth.login'))#redirect to login page if not logged in
    
    #sirf current user ke liye
    #fetch all tasks from the database, jisase hum unhe template me display kar saken
    tasks = Task.query.filter_by(user_id=user_id).order_by(Task.created_at.desc()).all() #fetching all tasks from the Task table
    #ab esko task page pe renbder kara denge aur sath me task bhi bhej denge jisae template me display kar saken
    return render_template('tasks.html', tasks=tasks)



#--------------------------------------------------route to add a new task ---------------------------------------

@tasks_bp.route('/add_task', methods=["POST"])
def add_task():
    #pahle check ker lete hain user logged in h ya nhi
    user_id = get_current_user_id() #ye function user id return karta h
    if 'user_id' not in session:
        flash('Please login to add tasks', 'warning') #flash message with category warning
        return redirect(url_for('auth.login')) #redirect to login page if not logged in
    
    #get task title from the form data
    title = request.form.get('title') #getting task title from form
    
    #Ager title h, to usko new task me add karte hain
    if not title:
        flash('Task title is required', 'danger')
        return redirect(url_for('tasks.view_tasks'))
    
    new_task = Task(title=title, status='Pending', user_id=user_id) #creating a new task object
    db.session.add(new_task) #adding the new task to the database session
    db.session.commit() #committing the session to save the task in the database
    flash('task added successfully', 'success') #flash mesage with category success
    #ab esko phir se home page pe redirect kr dete hain jaha sare tasks dikhaye jayenge
    return redirect(url_for('tasks.view_tasks')) #why tasks.view_tasks --> because view_tasks route is in tasks blueprint 




#------------------------------------------- route to update task status ------------------------------------------

@tasks_bp.route('/update_status/<int:task_id>', methods=["POST"])#why '/update_status/<int:task_id>' --> because we need to know which task to update, so we pass task_id as a parameter in the URL
def update_status(task_id): #route to update task status, why task_id --> because we need to know which task to update
    user_id = get_current_user_id() #ye function user id return karta h
    if 'user_id' not in session:
        flash('Please login to update tasks', 'warning')
        return redirect(url_for('auth.login'))

    # sirf usi task ko fetch karo jo current user ka hai
    task = Task.query.filter_by(id=task_id, user_id=user_id).first() #fetching the task from the database using the task_id
    
    if task: #if task exists, then update its status
        if task.status == 'Pending':# if current status is Pending then change into working
            task.status = 'Working'
        elif task.status == 'Working': #if task status is working then change into Done
            task.status = 'Done'
        else: #if task status is done then change into Pending
            task.status = 'Pending'
        
        db.session.commit() #committing the session to save the updated status in the database
        flash('Task status updated successfully', 'success') #flash message with category success
    else:
        flash("Task not found or you don't have permission", 'danger')

    #ab esko phir se home page pe redirect kr dete hain jaha sare tasks dikhaye jayenge
    return redirect(url_for('tasks.view_tasks')) #why tasks.view_tasks --> because view_tasks route is in tasks blueprint



#-----------------------------------------------------------route to delete a task--------------------------------------------

@tasks_bp.route('/delete_task/<int:task_id>', methods=["POST"]) #why '/delete_task/<int:task_id>' --> because we need to know which task to delete, so we pass task_id as a parameter in the URL
def delete_task(task_id): #route to delete a task, why task_id--> b/c we need to know which task to delete
    user_id = get_current_user_id() #ye function user id return karta h
    if 'user_id' not in session:
        flash('Please login to delete tasks', 'warning')
        return redirect(url_for('auth.login'))
    
    task = Task.query.filter_by(id=task_id, user_id=user_id).first() #fetching the task from the databse using the task id
    if task: #ager task exists kr rha h tbhi usko delete karenge
        db.session.delete(task) #deleting the task from the database sesion
        db.session.commit() #committing the session to save the changes in the session
        flash('task deleted successfully', 'success') #flash message with category success
    
    else:#ager task nhi mila to kuchh nhi karna
        flash("Task not found or you don't have permission", 'danger')
    #ager user deleted task ko undo krna chahta h to wo future me ek feature ho sakta h
    #ab esko phir se home page pe redirect kr dete hain jaha sare tasks
    return redirect(url_for('tasks.view_tasks')) #why tasks.view_tasks --> because view_tasks route is in tasks blueprint dikhaye jayenge



#--------------------------------------------------route to clear all tasks of logged-in user---------------------------------------

@tasks_bp.route('/clear_tasks', methods=["POST"]) #route to clear all tasks
def clear_tasks(): #function to clear to clear all tasks
    user_id = get_current_user_id() #ye function user id return karta h
    if 'user_id' not in session:
        flash('Please login to delete tasks', 'warning')
        return redirect(url_for('auth.login'))

    
    Task.query.filter_by(user_id=user_id).delete() #deleting all tasks from the Task table
    db.session.commit()#commiting the session to save the changes in the database
    flash('All tasks cleared successfully', 'success') #flash message with category success
    
    #ab esko phir se home page pe redirect kr dete hain jaha sare tasks dikhaye jayenge
    return redirect(url_for('tasks.view_tasks')) #why tasks.view_tasks --> because view_tasks route is in tasks blueprint
