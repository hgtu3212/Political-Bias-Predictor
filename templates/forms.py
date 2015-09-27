from wtforms import Form, BooleanField, TextField, validators, ValidationError

class textInputFromForm(Form):
	textinput = Form.TextField("Enter your news")
	def getText(self):
		return self.textinput
