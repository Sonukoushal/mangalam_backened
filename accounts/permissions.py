from rest_framework.permissions import BasePermission,SAFE_METHODS

#BasePermission = custom permission banane ka base class
#SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS'] → 

class IsSuperUserReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:    
            return True #Permission dedo-->allow all the user 
        else:
           return request.user and request.user.is_superuser 
                                                             
                                                          
        
