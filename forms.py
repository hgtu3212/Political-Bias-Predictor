from wtforms import Form, BooleanField, TextField, validators, ValidationError

class textInputFromForm(Form):
	textinput = TextField("Enter your news")
	def getText(self):
		return self.textinput
