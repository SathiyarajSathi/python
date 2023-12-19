from better_progress import Spinner

#...

spinner = Spinner.Spinner()
while True:
    #...
    spinner.next()
    print(spinner)





from better_progress import Bar

progress_bar = Bar.Bar(100000000000000)
print(progress_bar)
