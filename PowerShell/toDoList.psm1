new-Item $home\toDoList.txt
attrib +h $home\toDoList.txt

function Add-ToDo{
    param ([string]$newTask)
    echo $newTask >> $home\toDoList.txt
}

function Print-ToDo{
    Get-Content -Path $home\toDoList.txt
}

function Complete-TaskByName{
    param([string]$completedTask)
    attrib -h $home\toDoList.txt
    $todoList = Get-Content -Path $home\toDoList.txt
    $taskFound = $false
    $newList = @()
    if($todoList -is [array]){
        for ($i = 0; $i -lt $todoList.Length; $i++){
            if ($todoList[$i] -eq $completedTask){
                $todoList[$i] = ''
                $taskFound = $true

            }
        }
        for($i = 0; $i -lt $todoList.Length; $i++){
            if($todoList[$i] -eq ''){
                continue
            }
            else{
                $newList += $todoList[$i]
            }
        }
        if (-not $taskFound){
            write-host 'task not found, existing tasks are: '
            write-host $todoList
        }
        else{
            remove-item $home\toDoList.txt
            for ($i = 0; $i -lt $newList.Length; $i++){
                $newList[$i] >> $home\toDOList.txt
            }
        }
        if ($newList.Length -eq 0){
            new-Item $home\toDoList.txt | out-null
        }
        attrib +h $home\toDoList.txt
    }
    else{
        if ($completedTask -eq $todoList){
            remove-Item $home\toDoList.txt | out-null
            new-Item $home\toDoList.txt | out-null
            attrib +h $home\toDoList.txt
        }
        else{
            write-host 'task not found, existing task is: '
            write-host $todoList
        }
    }
}
