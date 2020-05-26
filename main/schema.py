from main.models import User,Symptoms,Specifics ,Guides,Role
from main.extensions import ma
# schemas
class SpecificSchema(ma.Schema):
    class Meta:
        fields = ('id','cough_degree','fever_degree','fatigue_degree','other_degree','symptom_id')

specific_schema = SpecificSchema()
specifics_schema = SpecificSchema(many=True)

class SymptomSchema(ma.Schema):
    class Meta:
        fields = ('id','cough','resp','fever','fatigue','other','user_id','date_added','specifics')
    
    specifics = ma.Nested(SpecificSchema)

symptom_schema = SymptomSchema()
symptoms_schema = SymptomSchema(many=True)

class GuideSchema(ma.Schema):
    class Meta:
        fields = ('name','done','info','time_lapse')

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','symptoms','days_left','guides','name','email','username','tel','country','state','address','age','sign_up_date','first_name','last_name','user_id')

    symptoms = ma.Nested(SymptomSchema,many=True)
    guides = ma.Nested(GuideSchema,many=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)

