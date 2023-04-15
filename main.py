from nicegui import ui

ui.label("show hide table ").classes("text-h4")


# CREATE COLUMNS AND ROWS FOR TABLE
columns = [
	{"name":"name","label":"you name","field":"name"},
	{"name":"age","label":"you age","field":"age"},
	]

rows= [
	{"name":"jujun","age":14},
	{"name":"dada","age":32},
	{"name":"oop","age":43},
	{"name":"jjii","age":21},

]
# NOW CREATE TABLE FROM YoU rows and column defined
table = ui.table(columns=columns,rows=rows,row_key="name")

show_hide_column = {column['name'] for column in columns }

# FUCNTION FOR CHANGE
def youchange(you_column,myshoworhide):
	print(you_column)
	print(myshoworhide)
	# NOW IF YOU SHOW TrUE VALUE FROM CHECKBOX THEN 
	if myshoworhide:
		# NOW ADD 
		show_hide_column.add(you_column['name'])

	# NOW IF YOU UNCHECKBOX THE CHECKBOX THEN REMOVE COLUMN
	else:
		show_hide_column.remove(you_column['name'])

	# NOW REFRESH AGAIN THE TABLE
	table._props['columns'] = [you_column for you_column in columns if you_column['name'] in show_hide_column]
	# NOW UPDATE AGAIN THE TABLE FOR SEE RESULT
	table.update() 



# NOW CREATE CHECKBOX NAME AND AGE FOR SHOW OR HIDE COLUMN
with ui.row():
	for x in columns:
		ui.checkbox(x['name'],value=True,on_change=lambda e,x=x:youchange(x,e.value))



# RUN IN DESKTOP MODE
ui.run(native=True)
