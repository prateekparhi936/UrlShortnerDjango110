import random
import string

def code_generator(size=6,chars=string.ascii_lowercase+string.digits):
	new_code=''
	for _ in range(size):
		new_code+=random.choice(chars)
	return new_code[0:size]	

def create_newcode(instance,size=6):
	new_code=code_generator(size=size)
	my_model=instance.__class__
	query_shortcode_exists=my_model.objects.filter(shortcode=new_code).exists()
	if query_shortcode_exists:
		return create_newcode(size=size)
	return new_code