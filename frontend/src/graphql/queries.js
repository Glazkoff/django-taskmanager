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
      taskSet {
        id
        storyPoints
        body
        status {
          id
          name
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
