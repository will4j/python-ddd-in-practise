# Created by william at 2023/7/16
Feature: 用小猪储蓄罐存钱
  你有一个小猪储蓄罐，可以往里面存钱。

  Scenario: 查看储蓄罐余额
    Given 储蓄罐里现在有5元
    When 我查看储蓄罐余额
    Then 储蓄罐余额是5元

  Scenario: 往储蓄罐存1元钱
    Given 储蓄罐里现在有10元
    When 我往储蓄罐里存入1元钱
    Then 储蓄罐余额是11元
