# Copyright (C) 2023 Avelino Bego
# 
# This file is part of XMLBuilder.
# 
# XMLBuilder is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
# 
# XMLBuilder is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with XMLBuilder.  If not, see <http://www.gnu.org/licenses/>.


from xmlbuilder import element

if __name__ == "__main__":
    b = element("eSocial")
    t = element("trabalhador")
    t.value("trab")
    b.evtTrabalhador(t).build()

    print(b)
