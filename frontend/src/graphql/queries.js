import gql from "graphql-tag";

export const BOARDS_IN_TEAM = gql`
  query ($teamId: ID) {
    boardsInTeam(teamId: $teamId) {
      id
      name
      statusSet {
        id
        name
        taskSet {
          id
          body
        }
      }
    }
  }
`;

export const BOARD_BY_ID = gql`
  query ($boardId: ID) {
    board(boardId: $boardId) {
      id
      name
      statusSet {
        id
        name
      }
      team {
        id
        name
        leader {
          id
          firstName
          lastName
          username
        }
        participants {
          id
          teamRole
          user {
            id
            username
            firstName
            lastName
          }
        }
        project {
          name
          prefix
          sprintSet {
            id
            name
          }
        }
      }
      taskSet {
        id
        storyPoints
        body
        status {
          id
        }
        sprint {
          id
          name
        }
        executor {
          firstName
          lastName
        }
      }
    }
  }
`;

export const BOARDS = gql`
  query {
    boards {
      id
      name
      statusSet {
        id
        name
        taskSet {
          id
          body
        }
      }
    }
  }
`;

export const TEAMS_LIST = gql`
  query {
    teams {
      id
      name
      boardSet {
        id
        name
      }
    }
  }
`;

export const UPDATE_SP = gql`
  mutation ($taskId: ID!, $storyPoints: Int!) {
    updateSp(taskId: $taskId, storyPoints: $storyPoints) {
      task {
        id
        storyPoints
      }
    }
  }
`;

export const UPDATE_STATUS = gql`
  mutation ($taskId: ID!, $statusId: ID!) {
    updateStatus(taskId: $taskId, statusId: $statusId) {
      task {
        id
        status {
          id
        }
      }
    }
  }
`;

export const CREATE_STATUS = gql`
  mutation ($boardId: ID!, $statusName: String!) {
    createStatus(boardId: $boardId, statusName: $statusName) {
      status {
        id
        name
      }
    }
  }
`;

export const CREATE_TASK = gql`
  mutation (
    $body: String!
    $executorId: ID
    $sprintId: ID
    $statusId: ID
    $storyPoints: Int
    $board: ID!
  ) {
    createTask(
      executor: $executorId
      body: $body
      sprint: $sprintId
      status: $statusId
      storyPoints: $storyPoints
      board: $board
    ) {
      task {
        id
        body
      }
    }
  }
`;
