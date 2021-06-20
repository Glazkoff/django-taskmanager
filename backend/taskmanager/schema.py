import graphene
import boards.schema
import teams.schema


class Query(boards.schema.Query, teams.schema.Query, graphene.ObjectType):
    pass


class Mutation(boards.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
