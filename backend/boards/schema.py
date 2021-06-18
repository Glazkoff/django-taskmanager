import graphene
from .models import Board, Task, Status, Comment
from .types import BoardType, TaskType, StatusType, CommentType
from .mutations import CreateTaskMutation


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    boards = graphene.List(BoardType)
    board = graphene.Field(BoardType, board_id=graphene.Int())
    boards_in_team = graphene.List(BoardType, team_id=graphene.Int())

    def resolve_boards(self, info, **kwargs):
        return Board.objects.all()

    def resolve_board(self, info, board_id):
        return Board.objects.get(pk=board_id)

    def resolve_boards_in_team(self, info, team_id):
        return Board.objects.filter(team=team_id)


class Mutation(graphene.ObjectType):
    create_task = graphene.Field(CreateTaskMutation)


schema = graphene.Schema(query=Query,)
