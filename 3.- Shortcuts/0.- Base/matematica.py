#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Jose Luis Jimenez Garcia"
__copyright__ = "Copyright 2020, Vielca Ingenieros"
__credits__ = ["Jose Luis"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Jose Luis"
__email__ = "pep.j@vielca.com"
__status__ = "Modulo en desarrollo"


 """ 
    Nombre de metodo:        _vel_prm
    Descripción:             Velocidad promedio de un objeto. El espacio que ha recorrido el objeto en un espacio de tiempo.
    Parametros entrada:      
        xi : Posición inicial.
        xj : Posición final.
        ti : Tiempo inicial.
        tj : Tiempo final.

    Parametros de retorno:   Devuelve la velocidad promedio del objeto.
 """ 
def _vel_prm(xi, xj, ti, tj):
    return ((xj - xi) / (tj-ty))

 """ 
    Nombre de metodo:        vel_prm_vc
    Descripción:             Velocidad promedio de un objeto. El espacio que ha recorrido el objeto siendo la velocidad constante.
    Parametros entrada:      
        vi : Velocidad inicial
        vj : Velocidad final
    Parametros de retorno:   Devuelve la velocidad promedio del objeto.
 """ 
def _vel_prm_vc(vi, vj):
    return ((vj - vi) / 2)

 """ 
    Nombre de metodo:        _vel_prm_v0
    Descripción:             Velocidad promedio siendo la aceleracion constante.
    Parametros entrada:      
        x : Instante
        t : Tiempo del objeto
    Parametros de retorno:   Devuelve la velocidad promedio del objeto.
 """ 
def _vel_prm_v0(x, t):
    return x/t

 """ 
    Nombre de metodo:        _vel
    Descripción:             Velocidad promedio atraves del producto de la acelaracion por el tiempo.
    Parametros entrada:      
        a : Aceleracion 
        t : Tiempo
    Parametros de retorno:   Devuelve la velocidad promedio del objeto.
 """ 
def _vel(a, t):
    return  a * t

 """ 
    Nombre de metodo:        _frz
    Descripción:             Calcula la fueza de un objeto.
    Parametros entrada:      
        m : Masa
        a : Aceleracion
    Parametros de retorno:   Se calcula como la masa por la aceleración.    
 """ 
def _frz(m, a)
    return m * a