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
          id
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
          id
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
      project {
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

export const DELETE_STATUS = gql`
  mutation ($statusId: ID!) {
    deleteStatus(statusId: $statusId) {
      ok
    }
  }
`;

export const UPDATE_TASK = gql`
  mutation (
    $taskId: ID!
    $body: String!
    $executorId: ID
    $sprintId: ID
    $statusId: ID
    $storyPoints: Int
  ) {
    updateTask(
      taskId: $taskId
      body: $body
      executor: $executorId
      sprint: $sprintId
      status: $statusId
      storyPoints: $storyPoints
    ) {
      task {
        id
        body
      }
    }
  }
`;

export const CREATE_BOARD = gql`
  mutation ($name: String!, $teamId: ID!) {
    createBoard(name: $name, teamId: $teamId) {
      board {
        id
        name
      }
    }
  }
`;

export const USERS = gql`
  {
    users {
      id
      firstName
      lastName
      username
    }
  }
`;

export const PROJECTS = gql`
  {
    projects {
      id
      name
      leader {
        id
        username
        lastName
        firstName
        lastLogin
      }
      prefix
      draft
      sprintSet {
        id
        name
      }
      settings {
        teamLimit
        sprintLimit
      }
      teams {
        id
        name
      }
    }
  }
`;

export const CREATE_TEAMS = gql`
  mutation (
    $name: String!
    $leaderId: ID!
    $projectId: ID!
    $participants: [ID]
  ) {
    createTeam(
      name: $name
      leaderId: $leaderId
      projectId: $projectId
      participants: $participants
    ) {
      team {
        id
        name
      }
    }
  }
`;

export const CREATE_PROJECT = gql`
  mutation ($name: String!, $prefix: String!, $teams: [ID], $leaderId: ID!) {
    createProject(
      name: $name
      prefix: $prefix
      teams: $teams
      leaderId: $leaderId
    ) {
      project {
        id
        name
      }
    }
  }
`;

export const CREATE_SPRINT = gql`
  mutation (
    $name: String!
    $aim: String!
    $projectId: ID!
    $startDate: String
    $finishDate: String
  ) {
    createSprint(
      name: $name
      aim: $aim
      projectId: $projectId
      startDate: $startDate
      finishDate: $finishDate
    ) {
      sprint {
        id
        name
      }
    }
  }
`;

export const CREATE_USER_AUTH = gql`
  mutation ($username: String!, $password: String!) {
    createUserAuth(username: $username, password: $password) {
      user {
        id
        username
        firstName
        lastName
      }
      employee {
        teamRole
      }
      isOk
    }
  }
`;
