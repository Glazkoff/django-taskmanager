import graphene
from .models import Board, Task, Status, Comment
from .types import BoardType, TaskType, StatusType, CommentType
from .mutations import CreateTaskMutation, UpdateStoryPointsMutation, UpdateStatusMutation, CreateStatusMutation, DeleteStatusMutation, UpdateTaskMutation, CreateBoardMutation, CreateTeamMutation, CreateProjectMutation, CreateSprintMutation, CreateUserAuthMutation, DeleteProjectMutation


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    boards = graphene.List(BoardType)
    board = graphene.Field(BoardType, board_id=graphene.ID())
    boards_in_team = graphene.List(BoardType, team_id=graphene.ID())

    def resolve_boards(self, info, **kwargs):
        return Board.objects.all()

    def resolve_board(self, info, board_id):
        return Board.objects.get(pk=board_id)

    def resolve_boards_in_team(self, info, team_id):
        return Board.objects.filter(team=team_id)


class Mutation(graphene.ObjectType):
    # create_task = graphene.Field(CreateTaskMutation)
    update_sp = UpdateStoryPointsMutation.Field()
    update_status = UpdateStatusMutation.Field()
    create_status = CreateStatusMutation.Field()
    delete_status = DeleteStatusMutation.Field()
    create_task = CreateTaskMutation.Field()
    update_task = UpdateTaskMutation.Field()
    create_board = CreateBoardMutation.Field()
    create_team = CreateTeamMutation.Field()
    create_project = CreateProjectMutation.Field()
    create_sprint = CreateSprintMutation.Field()
    create_user_auth = CreateUserAuthMutation.Field()
    delete_project = DeleteProjectMutation.Field()


schema = graphene.Schema(query=Query,)
