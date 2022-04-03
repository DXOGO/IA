

# Guiao de representacao do conhecimento
# -- Redes semanticas
# 
# Inteligencia Artificial & Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2020
# v1.9 - 2019/10/20
#


# Classe Relation, com as seguintes classes derivadas:
#     - Association - uma associacao generica entre duas entidades
#     - Subtype     - uma relacao de subtipo entre dois tipos
#     - Member      - uma relacao de pertenca de uma instancia a um tipo
#

from collections import Counter


class Relation:
    def __init__(self,e1,rel,e2):
        self.entity1 = e1
#       self.relation = rel  # obsoleto
        self.name = rel # rel entre e1 e e2
        self.entity2 = e2
    def __str__(self):
        return self.name + "(" + str(self.entity1) + "," + str(self.entity2) + ")"
    def __repr__(self):
        return str(self)


# Subclasse Association
class Association(Relation):
    def __init__(self, e1, assoc, e2):
        Relation.__init__(self, e1, assoc, e2)
        
#   Exemplo:
#   a = Association('socrates','professor','filosofia') -> Association(entity1, name, entity2)
#                                                       -> socrates(entity1) é professor(associaçao) de filosofia(entity2)

class AssocOne(Association):    # (!) 15)
    one = dict()

    def __init__(self, e1, assoc, e2):
        if assoc not in AssocOne.one:
            AssocOne.one[assoc] = dict()
        assert e2 not in AssocOne.one[assoc] or AssocOne.one[assoc][e2].entity1 == e1
        AssocOne.one[assoc][e2] = self

        Association.__init__(self, e1, assoc, e2)

class AssocNum(Association):    # (!) 15)
    def __init__(self, e1, assoc, e2):
        assert isinstance(e2, (int, float))
        Association.__init__(self, e1, assoc, e2)
        

# Subclasse Subtype
class Subtype(Relation):
    def __init__(self,sub,super):
        Relation.__init__(self,sub,"subtype",super)
#   Exemplo:
#   s = Subtype('homem','mamifero')  -> Subtype(subtype, supertype), homem(subtype) é mamifero(supertype)


# Subclasse Member
class Member(Relation):
    def __init__(self,obj,type):
        Relation.__init__(self,obj,"member",type)
#   Exemplo:
#   m = Member('socrates','homem')  -> Member(obj, type), socrates(obj) é homem(type)


# classe Declaration
# -- associa um utilizador a uma relacao por si inserida na rede semantica
class Declaration:
    def __init__(self,user,rel):
        self.user = user
        self.relation = rel # (!) vai ser association, subtype or member
    def __str__(self):
        return "decl("+str(self.user)+","+str(self.relation)+")"
    def __repr__(self):
        return str(self)


###   Exemplos:

#   da = Declaration('descartes',a)
# >>> str(da)
# 'decl(descartes, professor(socrates, filosofia))'
# onde a= Association('socrates','professor','filosofia')

#   ds = Declaration('darwin',s)
# >>> str(ds)
# 'decl(darwin, subtype(homem, mamifero))'
# onde s= Subtype('homem','mamifero')

#   dm = Declaration('descartes',m)
# >>> str(dm)
# 'decl(descartes, member(socrates, homem))'
# onde s= Member('socrates', 'homem')


# classe SemanticNetwork
# -- composta por um conjunto de declaracoes
#    armazenado na forma de uma lista
#
class SemanticNetwork:
    def __init__(self,ldecl=None):
        self.declarations = [] if ldecl==None else ldecl
    
    def __str__(self):
        return str(self.declarations)
    
    def insert(self,decl):
        self.declarations.append(decl)
    
    # obter informação local (ou seja, propriedades não herdadas) sobre as várias entidades presentes na rede
    # questionar a rede semântica sobre as declarações existentes
    def query_local(self,user=None,e1=None,rel=None,e2=None, rel_type=None):
        self.query_result = \
            [ d for d in self.declarations
                if  (user == None or d.user==user)
                and (e1 == None or d.relation.entity1 == e1)
                and (rel == None or d.relation.name == rel)
                and (e2 == None or d.relation.entity2 == e2) 
                and (rel_type == None or isinstance(d.relation,rel_type))   # (!) added for 11) and after
            ]
        return self.query_result
    
    def show_query_result(self):
        for d in self.query_result:
            print(str(d))

# >>> z=Semantic Network()
# >>> z.insert(da)
# >>> z.insert(dm)
# >>> z.insert(Declaration (’descartes’, Member (’platao’ , ’homem’)))
# >>> z.querylocal(user=’descartes’, rel = ’member’)
# .......
# >>> z.show_query_result()
# decl(descartes, member(socrates, homem))
# decl(descartes, member(platao, homem))
# (!) 'da' n aparece pq nao é rel='member' mas sim rel='association'

    
    
    # (!) 1) Programe uma função que devolva a lista (dos nomes) das associações existentes
    def list_associations(self):
        association = []
        for decl in self.declarations:
            if isinstance(decl.relation, Association) and decl.relation.name not in association:
                association.append(decl.relation.name)
        return association
    # or return list(set([d.relation.name for d in self.declarations if isinstance(d.relation, Association)]))

    
    
    # (!) 2) Programe uma função que devolva a lista dos objectos cuja existência pode ser inferida da rede, 
    #        ou seja, uma lista das entidades declaradas como instâncias de tipos.
            
    #        membro = instância de tipo (A é membro de B=A é uma instância de B)
    def list_objects(self):    
        entities = []
        for decl in self.declarations:
            if isinstance(decl.relation, Member) and decl.relation.entity1 not in entities :
                entities.append(decl.relation.entity1)
        return entities
    # or return list(set([d.relation.entity1 for d in self.declarations if isinstance(d.relation, Member)]))

    
    
    # (!) 3) Programe uma função que devolva a lista de utilizadores existentes na rede.
    def list_users(self):
        users = []
        for decl in self.declarations:
            if decl.user not in users:
                users.append(decl.user)
        return users
    # or return list(set([d.user for d in self.declarations]))

    
    
    # (!) 4) Programe uma função que devolva a lista de tipos existente na rede.
    def list_types(self):
        types = []
        for decl in self.declarations:
            if isinstance(decl.relation, (Member, Subtype)) and decl.relation.entity2 not in types:
                    types.append(decl.relation.entity2) # entity2 é o tipo "super" tanto de member como subtype
            if isinstance(decl.relation, Subtype) and decl.relation.entity1 not in types:
                    types.append(decl.relation.entity1) # entity1 de subtype pode tmb ser "super" tipo de outra relaçao
        return types                                    # ex: homem-subtype-mamifero e mamifero-subtype-vertebrado
    # or return list(set([d.relation.entity2 for d in self.declarations if isinstance(d.relation, Member) or isinstance(d.relation, Subtype)] 
    #                   + [d.relation.entity1 for d in self.declarations if isinstance(d.relation, Subtype)]))

    
    
    # (!) 5) Programe uma função que, dada uma entidade, devolva a lista (dos nomes) das associações localmente declaradas.
    def list_local_associations(self, e):
        local = []
        for decl in self.declarations:
            if isinstance(decl.relation, Association) and (decl.relation.entity1 == e or decl.relation.entity2 == e):
                if decl.relation.name not in local:
                    local.append(decl.relation.name)
        return local

    # or return list(set([d.relation.name for d in self.declarations if isinstance(d.relation, Association) 
    #                   and (d.relation.entity1 == e or d.relation.entity2 == e)]))

    
    
    # (!) 6) Programe uma função que, dado um utilizador, devolva a lista (dos nomes) das relações por ele declaradas
    def list_relations_by_user(self,u):
        user_list = []
        for decl in self.declarations:
            if decl.user == u and decl.relation.name not in user_list:
                user_list.append(decl.relation.name)

        return user_list
    # or return list(set([d.relation.name for d in self.declarations if d.user == user]))

    
    
    # (!) 7) Programe uma função que, dado um utilizador, devolva o número de associações diferentes
    #        por ele utilizadas nas relações que declarou.
    def associations_by_user(self,u):
        assoc = []
        for decl in self.declarations:
            if decl.user == u and isinstance(decl.relation, Association) and decl.relation.name not in assoc:
                assoc.append(decl.relation.name)
        
        return len(assoc)
    # or return len(set([d.relation.name for d in self.declarations if d.user == user and isinstance(d.relation, Association)]))

    
    
    # (!) 8) Programe uma função que, dada uma entidade, devolva uma lista de tuplos, em que cada tuplo 
    #        contém (o nome de) uma associação localmente declarada e o utilizador que a declarou
    def list_local_associations_by_user(self, e):
        return list(set([(d.relation.name, d.user) for d in self.declarations if isinstance(d.relation, Association) \
                     and (d.relation.entity1 == e or d.relation.entity2 == e)]))

    
    
    # (!) 9) Uma entidade A é predecessora (ou ascendente) de uma entidade B se existir uma cadeia 
    #        de relações Member e/ou Subtype que liguem B a A. 
    #        Programe uma função que, dadas 2 entidades (dois tipos, ou um tipo e um objecto), 
    #        devolva True 1ª predecesse 2º, e False caso contrário.
    def predecessor(self, e1, e2):  # alinea 9)
        relations = []
        for decl in self.declarations:
            if isinstance(decl.relation, (Member, Subtype)) and decl.relation.entity1 == e2:
                if decl.relation.name not in relations:
                    relations.append(decl.relation)
        
        if [r for r in relations if r.entity2 == e1] != []:
            return True

        return any([self.predecessor(e1, r.entity2) for r in relations])
    
    
    # (!) 10) Programe uma função que, dadas duas entidades (dois tipos, ou um tipo e um objecto),
    #         em que a primeira é predecessora da segunda, devolva uma lista composta pelas entidades
    #         encontradas no caminho desde a primeira até à segunda entidade. Caso a primeira entidade
    #         não seja predecessora da segunda, a função retorna None
    def predecessor_path(self, e1, e2): 
        relations = [d.relation.entity2 for d in self.declarations 
                        if isinstance(d.relation, (Member, Subtype)) and d.relation.entity1==e2]

        if e1 in relations:    
            return [e1, e2]

        for path in [self.predecessor_path(e1,p) for p in relations]:
            if path:
                return path + [e2]
        
        return None

    
    
    # (!) 11) Desenvolva uma nova função query() na classe SemanticNetwork que permita obter todas
    #         as declarações de associações locais ou herdadas por uma entidade. A função recebe
    #         como entrada a entidade e, opcionalmente, o nome da associação.
    def query(self, entity, assoc = None):
        pds = self.query_local(e1=entity, rel_type=(Member, Subtype))

        pds_assoc = []
        for e2 in [d.relation.entity2 for d in pds]:
            pds_assoc.extend(self.query(e2 , assoc)) 

        local_assoc = self.query_local(e1=entity, rel=assoc ,rel_type=Association)

        return pds_assoc + local_assoc
    

    
    
    # (!) 12) Desenvolva uma nova função de consulta, query cancel () , similar à função query() , mas em
    #         que existe cancelamento de herança. Neste caso, quando uma associação está declarada
    #         numa entidade, a entidade não herdará essa associação das entidades predecessoras. A
    #         função recebe como entrada a entidade e o nome da associação.
    def query_cancel(self, entity, assoc):
        pds = self.query_local(e1=entity, rel_type=(Member, Subtype))

        local_assoc = self.query_local(e1=entity, rel=assoc ,rel_type=Association)

        pds_assoc = []
        for e2 in [d.relation.entity2 for d in pds]:
            pds_assoc.extend([d for d in self.query_cancel(e2 , assoc) if d.relation.name not in [l.relation.name for l in local_assoc]]) 

        return pds_assoc + local_assoc
        
        
    
    
    # (!) 13) Desenvolva uma função query down() na classe SemanticNetwork que, dado um tipo e (o nome de) uma associação, 
    #         devolva uma lista com todas as declarações dessa associação em entidades descendentes desse tipo.
    def query_down(self, entity, assoc, first=True):
        descendents = self.query_local(e2 = entity, rel_type=(Member, Subtype))
        descendents_assoc = []

        for e1 in [d.relation.entity1 for d in descendents]:
            descendents_assoc.extend(
                self.query_down(e1, assoc, False)
            )

        if first:
            local_assoc = []
        else:    
            local_assoc = self.query_local(e1=entity, rel=assoc)

        return descendents_assoc + local_assoc
    
    
    
    
    # (!) 14) Por vezes, na ausência de informação geral conhecida, pode ser útil usar inferência por indução. 
    #         Neste caso, usa-se informação sobre entidades mais especı́ficas (subtipos e/ou instâncias) para inferir 
    #         propriedades gerais de um tipo. Assim, desenvolva uma função query induce () que, dado um tipo e (o nome de) uma associação, 
    #         devolva o valor mais frequente dessa associação nas entidades descendentes.
    def query_induce(self, entity, assoc):
        descendents = self.query_down(entity, assoc)

        assoc_values = [d.relation.entity2 for d in descendents]

        for c,_ in Counter(assoc_values).most_common(1):
            return c
     
     
        
        
    # Até agora, considerámos que as associações admitem múltiplos valores. Por exemplo, a associação gosta pode admitir vários 
    # valores (pode-se gostar de peixe e de carne). Num sistema profissional, encontram-se outros tipos de associações. 
    # Há associações que admitem apenas um valor. Por exemplo, pai admite apenas um valor (o pai da pessoa em causa). 
    # Já no caso de associações com valor numérico (por exemplo altura ou peso ), a existência de vários valores declarados pode ser tratada como uma boa aproximação à verdade.
    
    # Desenvolva duas classes derivadas da classe Relation para representar associações com com um único valor (classe AssocOne) 
    # e associações com valores numéricos (classe AssocNum).    
    
    # (!) 15) Desenvolva uma nova função query_local_assoc() na classe SemanticNetwork , a qual permite fazer consultas de valores das associações
    #         locais de uma dada entidade, devendo processar os diferentes tipos de associações
    def query_local_assoc(self, entity, assoc):
        local = self.query_local(e1=entity, rel=assoc, rel_type=Association)
        for d in local:
            if isinstance(d.relation, AssocNum):
                return sum([d.relation.entity2 for d in local]) / len(local)
            if isinstance(d.relation, AssocOne):
                for c, v in Counter([d.relation.entity2 for d in local]).most_common(1):
                    return c, v / len(local)
                return None
            total_freq = 0
            res = list()
            for c, v in Counter([d.relation.entity2 for d in local]).most_common():
                res.append((c, v / len(local)))
                total_freq += v / len(local)
                if total_freq > 0.75:
                    return res


    
    
    # (!) 16) Neste tipo de rede semântica, dada a acumulação de declarações de vários interlocutores,
    #         podem ocorrer inconsistências no conhecimento registado. Existindo divergência nos valores
    #         atribuı́dos a uma associação numa entidade, faz sentido levar também em conta os valores
    #         herdados. Assim, desenvolva uma função query assoc value () que, dada uma entidade, E,
    #         e (o nome de) uma associação, A, devolva o valor, V , dessa associação nessa entidade
    def query_assoc_value(self, E, A):
        local = self.query_local(e1=E, rel=A, rel_type=Association)
        
        if len(local) and all([local[0].relation.entity2 == l.relation.entity2 for l in local]):
            return local[0].relation.entity2
        
        pds = self.query_local(e1=E, rel_type=(Member, Subtype))
        herdados = []
        for e2 in [d.relation.entity2 for d in pds]:
            herdados.extend(self.query(e2 , A)) 

        def perc_v(assocs, v):
            if(len(assocs)):
                return [a.relation.entity2 for a in assocs].count(v)
            return 0

        maximizacao = []
        for v in [a.relation.entity2 for a in local + herdados]:
            maximizacao.append((v, (perc_v(local, v) + perc_v(herdados, v)) /2))

        v, _ = max(maximizacao,key= lambda x: x[1])

        return v