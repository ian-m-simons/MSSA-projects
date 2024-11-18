new-Item C:\Users\ianms\toDoList.txt
attrib +h C:\Users\ianms\toDoList.txt

function Add-ToDo{
    param ([string]$newTask)
    echo $newTask >> C:\Users\ianms\toDoList.txt
}

function Print-ToDo{
    Get-Content -Path C:\Users\ianms\toDoList.txt
}

function Complete-TaskByName{
    param([string]$completedTask)
    attrib -h C:\Users\ianms\toDoList.txt
    $todoList = Get-Content -Path C:\Users\ianms\toDoList.txt
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
            remove-item C:\Users\ianms\toDoList.txt
            for ($i = 0; $i -lt $newList.Length; $i++){
                $newList[$i] >> C:\Users\ianms\toDOList.txt
            }
        }
        if ($newList.Length -eq 0){
            new-Item C:\Users\ianms\toDoList.txt | out-null
        }
        attrib +h C:\Users\ianms\toDoList.txt
    }
    else{
        if ($completedTask -eq $todoList){
            remove-Item C:\Users\ianms\toDoList.txt | out-null
            new-Item C:\Users\ianms\toDoList.txt | out-null
            attrib +h C:\Users\ianms\toDoList.txt
        }
        else{
            write-host 'task not found, existing task is: '
            write-host $todoList
        }
    }
}