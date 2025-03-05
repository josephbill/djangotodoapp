from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
"""these functionalities take care of CRUD :-)"""
def task_list(request):
    """this function collects the task items"""
    # [] empty list is a default if tasks are empty
    tasks = request.session.get('tasks', [])
    # the render() function returns a .html template
    return render(request, 'todolistapp/task_list.html',
                  {"tasks" : tasks})

def add_task(request):
    "adds new task"
    if request.method == "POST":
        task = request.POST.get("task")
        # checking if task has been captured
        if task:
            # fetch the existing tasks
            tasks = request.session.get('tasks', [])
            #add the new task to above list
            tasks.append({'task' : task, 'done': False})
            #save the new list to the current session
            request.session['tasks'] = tasks
            #notify user
            messages.success(request,"Task added")
        else:
            messages.error(request,"Task not found")
    #redirect is different from render , render loads the
    # template , redirects simply change the web address to
    # given location
    return redirect('task_list')


def delete_task(request, index):
    """delete the task at the given index"""
    tasks = request.session.get('tasks', [])
    if 0 <= index < len(tasks):
       del tasks[index]
       #save the new tasks
       request.session['tasks'] = tasks
       messages.success(request,"Task deleted")
    else:
        messages.error(request,"Task not found")
    return redirect('task_list')

def mark_complete(request, index):
    """mark the task at the given index as complete"""
    tasks = request.session.get('tasks', [])
    if 0 <= index < len(tasks):
        tasks[index]['done'] = True
        request.session['tasks'] = tasks
        messages.success(request,"Task marked as complete")
    else:
        messages.error(request,"Task not found")
    return redirect('task_list')













