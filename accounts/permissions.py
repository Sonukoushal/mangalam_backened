from rest_framework.permissions import BasePermission,SAFE_METHODS

#BasePermission = custom permission banane ka base class
#SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS'] → ye wo methods hain jo read-only hote hain

class IsSuperUserReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:    #request.method matlab vo method jo frontened se ya postman se aayi ho 
            return True #Permission dedo-->allow all the user 
        else:
           return request.user and request.user.is_superuser #request.user --> instance hota hai logged in user ka 
                                                             #request.user.is_superuser --> kya vo superuser hai?
                                                             #logical operator apne aap return valur true ya false me bhejte hai agar dono condition true hai to true value return kar deta hai
        