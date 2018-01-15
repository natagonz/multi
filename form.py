from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField ,TextAreaField, IntegerField, DateField, SelectField,SubmitField
from wtforms.validators import InputRequired, EqualTo, Email, Length
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf.file import FileField, FileAllowed, FileRequired

images = UploadSet("images",IMAGES)


class UserRegisterForm(FlaskForm):
	username = StringField("Username",validators=[InputRequired(),Length(max=100)])
	email = StringField("Email",validators=[InputRequired(),Length(max=100)])
	password = PasswordField("Password",validators=[InputRequired(),Length(min=6)])


class UserLoginForm(FlaskForm):
	email = StringField("Email",validators=[InputRequired()])
	password = PasswordField("Password",validators=[InputRequired()])



class AddMemberForm(FlaskForm):
	username = StringField("Username",validators=[InputRequired(),Length(max=100)])
	email = StringField("Email",validators=[InputRequired(),Length(max=100)])
	password = PasswordField("Password",validators=[InputRequired(),Length(min=6)])
	phone = StringField("Telepon",validators=[Length(max=100)])
	mobil = StringField("Mobil",validators=[Length(max=100)])
	plat =  StringField("Plat",validators=[Length(max=100)])
	date = DateField("Tanggal",format="%m/%d/%Y")	

class EditMemberForm(FlaskForm):
	username = StringField("Username",validators=[InputRequired(),Length(max=100)])
	email = StringField("Email",validators=[InputRequired(),Length(max=100)])	
	phone = StringField("Telepon",validators=[Length(max=100)])
	mobil = StringField("Mobil",validators=[Length(max=100)])
	plat =  StringField("Plat",validators=[Length(max=100)])
	date = DateField("Tanggal",format="%m/%d/%Y")	
	renew = DateField("Aktif Sampai",format="%m/%d/%Y")



class BookingStatusForm(FlaskForm):
	status = SelectField("",choices= [("Belum Selesai","Belum Selesai"),("Selesai","Selesai")])	


class DeleteAntreanForm(FlaskForm):
	submit = SubmitField("Hapus Antrean")	


class ForgotPasswordForm(FlaskForm):
	email = StringField("Email",validators=[InputRequired(),Length(max=100)]) 


class ResetPasswordForm(FlaskForm):
	password = PasswordField("Password",validators=[InputRequired(),Length(min=6,max=100)])



class AddPackageForm(FlaskForm):
	name = StringField("Paket",validators=[Length(max=100),InputRequired()])
	price = IntegerField("Harga Rp",validators=[InputRequired()]) 	
	
	
class AddGalleryForm(FlaskForm):
	image = FileField("Upload Photo",validators=[FileAllowed(images,"Images Only")])
	description = StringField("Deskripsi",validators=[Length(max=200)])





